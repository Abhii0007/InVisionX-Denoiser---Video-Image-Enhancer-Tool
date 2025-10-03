
import sys
import cv2
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QSlider, QStyle, QHBoxLayout, QGraphicsView, QGraphicsScene
)
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QGraphicsVideoItem
from PySide6.QtCore import Qt, QUrl


class VideoViewer(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setScene(QGraphicsScene(self))
        self.videoItem = QGraphicsVideoItem()
        self.scene().addItem(self.videoItem)

        # Enable pan & zoom
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)

    def wheelEvent(self, event):
        """Zoom with mouse wheel"""
        zoomFactor = 1.2
        if event.angleDelta().y() > 0:
            self.scale(zoomFactor, zoomFactor)
        else:
            self.scale(1 / zoomFactor, 1 / zoomFactor)


class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Player (Zoom + Pan + Frame Step)")
        self.setGeometry(200, 200, 900, 600)

        self.fps = 30  # default fallback FPS

        # Media player
        self.mediaPlayer = QMediaPlayer(self)
        self.audioOutput = QAudioOutput()
        self.mediaPlayer.setAudioOutput(self.audioOutput)

        # Custom video viewer
        self.viewer = VideoViewer()
        self.mediaPlayer.setVideoOutput(self.viewer.videoItem)

        # Controls
        self.openButton = QPushButton("Open")
        self.openButton.clicked.connect(self.open_file)

        self.playButton = QPushButton(self.style().standardIcon(QStyle.SP_MediaPlay), "")
        self.playButton.clicked.connect(self.toggle_play)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        # Layouts
        controlLayout = QHBoxLayout()
        controlLayout.addWidget(self.openButton)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.slider)

        layout = QVBoxLayout()
        layout.addWidget(self.viewer)
        layout.addLayout(controlLayout)
        self.setLayout(layout)

        # Signals
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def open_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Open Video File", "", "Video Files (*.mp4 *.avi *.mkv)")
        if file:
            # Extract FPS using OpenCV
            cap = cv2.VideoCapture(file)
            fps_val = cap.get(cv2.CAP_PROP_FPS)
            if fps_val > 0:
                self.fps = fps_val
            cap.release()

            self.mediaPlayer.setSource(QUrl.fromLocalFile(file))
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def toggle_play(self):
        if self.mediaPlayer.playbackState() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        else:
            self.mediaPlayer.play()
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def keyPressEvent(self, event):
        """Keyboard shortcuts"""
        frame_time = 1000 / self.fps  # ms per frame

        if event.key() == Qt.Key_Space:  # Spacebar → Play/Pause
            self.toggle_play()

        elif event.key() == Qt.Key_Right:  # Right arrow → forward 5 frames
            new_pos = self.mediaPlayer.position() + int(5 * frame_time)
            self.mediaPlayer.setPosition(new_pos)

        elif event.key() == Qt.Key_Left:  # Left arrow → backward 5 frames
            new_pos = max(0, self.mediaPlayer.position() - int(5 * frame_time))
            self.mediaPlayer.setPosition(new_pos)

        else:
            super().keyPressEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec())
