import sys
import os
import subprocess
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
    QFileDialog, QMessageBox, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
)
from PySide6.QtGui import QPixmap, QWheelEvent, QMouseEvent
from PySide6.QtCore import Qt, QPointF
from PySide6.QtCore import QThread, Signal, QObject
from PySide6.QtWidgets import QProgressBar
from PySide6.QtWidgets import QSlider, QLabel
from PySide6.QtCore import Qt


from PySide6.QtGui import QPixmap, QWheelEvent, QMouseEvent, QPainter


from PySide6.QtCore import QObject, Signal
import subprocess

class UpscaleWorker(QObject):
    output_signal = Signal(str)  # To send each output line
    finished = Signal(bool, str)  # success, error_message

    def __init__(self, exe_path, input_path, output_path, scale=2):
        super().__init__()
        self.exe_path = exe_path
        self.input_path = input_path
        self.output_path = output_path
        self.scale = scale

    def run(self):
        cmd = [
            self.exe_path,
            "-i", self.input_path,
            "-o", self.output_path,
            "-n", "realesr-animevideov3",
            "-s", str(self.scale)
        ]


        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,  # merge stderr into stdout
                text=True,
                bufsize=1
            )

            # Stream output line by line
            for line in iter(process.stdout.readline, ''):
                if line:
                    self.output_signal.emit(line.rstrip())

            process.stdout.close()
            returncode = process.wait()

            if returncode == 0:
                self.finished.emit(True, "")
            else:
                self.finished.emit(False, f"Exited with code {returncode}")

        except Exception as e:
            self.finished.emit(False, str(e))




class ImageViewer(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setScene(QGraphicsScene(self))
        self.pixmap_item = QGraphicsPixmapItem()
        self.scene().addItem(self.pixmap_item)

        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setRenderHint(QPainter.Antialiasing)  # ✅ Fixed here
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.scale_factor = 1.0


    def set_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.pixmap_item.setPixmap(pixmap)
        self.scene().setSceneRect(pixmap.rect())
        self.reset_transform()

    def reset_transform(self):
        self.resetTransform()
        self.scale_factor = 1.0

    def wheelEvent(self, event: QWheelEvent):
        zoom_in_factor = 1.25
        zoom_out_factor = 1 / zoom_in_factor

        if event.angleDelta().y() > 0:
            zoom_factor = zoom_in_factor
        else:
            zoom_factor = zoom_out_factor

        self.scale(zoom_factor, zoom_factor)
        self.scale_factor *= zoom_factor

from PySide6.QtWidgets import QTextEdit,QHBoxLayout
import re
class RealESRGANGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Real-ESRGAN Image Upscaler")
        self.setGeometry(100, 100, 1000, 600)  # Make wider to fit both widgets

        # Image viewer widget
        self.image_viewer = ImageViewer()
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)

                # Label to show slider value
        self.scale_label = QLabel("Upscale: 2x")
        self.scale_label.setAlignment(Qt.AlignCenter)

        # Slider from 1 to 4 (x1 to x4)
        self.scale_slider = QSlider(Qt.Horizontal)
        self.scale_slider.setMinimum(2)
        self.scale_slider.setMaximum(4)

        self.scale_slider.setValue(2)  # Default 2x
        self.scale_slider.setTickInterval(1)
        self.scale_slider.setTickPosition(QSlider.TicksBelow)

        # Update label when slider moves
        self.scale_slider.valueChanged.connect(self.update_scale_label)


        # Terminal output widget
        self.console_output = QTextEdit()
        self.console_output.setReadOnly(True)
        self.console_output.setLineWrapMode(QTextEdit.NoWrap)
        self.console_output.setMinimumWidth(400)

        # Buttons
        self.btn_import = QPushButton("Import Image")
        self.btn_convert = QPushButton("Convert Image")
        self.btn_save = QPushButton("Save Image")

        # Layouts
        main_layout = QVBoxLayout()
        
        # Horizontal layout for image + console
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.image_viewer)
        h_layout.addWidget(self.console_output)

        main_layout.addLayout(h_layout)

        # Add buttons below
        main_layout.addWidget(self.progress_bar)
        main_layout.addWidget(self.btn_import)
        main_layout.addWidget(self.btn_convert)
        main_layout.addWidget(self.btn_save)
        main_layout.addWidget(self.scale_label)
        main_layout.addWidget(self.scale_slider)


        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # File paths
        self.input_path = ""
        self.output_path = os.path.join("realesrgan", "output.png")

        # Event bindings
        self.btn_import.clicked.connect(self.import_image)
        self.btn_convert.clicked.connect(self.convert_image)
        self.btn_save.clicked.connect(self.save_image)
        
        
    def update_scale_label(self, value):
        self.scale_label.setText(f"Upscale: {value}x")


    def import_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.input_path = file_path
            self.image_viewer.set_image(file_path)
        self.progress_bar.setValue(0)
        self.console_output.clear()



    def convert_image(self):
        self.progress_bar.setValue(0)

        if not self.input_path:
            QMessageBox.warning(self, "Error", "Please import an image first.")
            return

        exe_path = os.path.join("realesrgan", "realesrgan-ncnn-vulkan.exe")
        if not os.path.exists(exe_path):
            QMessageBox.critical(self, "Error", f"{exe_path} not found.")
            return

        self.console_output.clear()

        self.progress = QMessageBox(self)
        self.progress.setWindowTitle("Processing")
        self.progress.setText("Upscaling in progress...\nPlease wait.")
        self.progress.setStandardButtons(QMessageBox.NoButton)
        self.progress.show()

        self.thread = QThread()
        scale = self.scale_slider.value()
        self.worker = UpscaleWorker(exe_path, self.input_path, self.output_path, scale)

        self.worker.moveToThread(self.thread)

        # 👇 Connect signal to GUI method
        self.worker.output_signal.connect(self.append_console_text)
        self.worker.finished.connect(self.on_upscale_done)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()


    

    def append_console_text(self, text):
        self.console_output.append(text)

        # Scroll to the bottom
        scrollbar = self.console_output.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

        # Check if line is a percentage (e.g., "66.67%")
        match = re.match(r"^\s*(\d+(?:\.\d+)?)\s*%", text)
        if match:
            percent = float(match.group(1))
            self.progress_bar.setValue(int(percent))


        
    def on_upscale_done(self, success, error_msg):
        self.progress.hide()
        self.progress_bar.setValue(100 if success else 0)


        if success:
            QMessageBox.information(self, "Success", "Image upscaled successfully.")
            self.image_viewer.set_image(self.output_path)
        else:
            QMessageBox.critical(self, "Upscaling Failed", error_msg)

        

    def save_image(self):
        if not os.path.exists(self.output_path):
            QMessageBox.warning(self, "Error", "No converted image to save.")
            return

        save_path, _ = QFileDialog.getSaveFileName(self, "Save Image As", "upscaled.png", "PNG Files (*.png);;JPEG Files (*.jpg *.jpeg)")
        if save_path:
            try:
                with open(self.output_path, "rb") as f_src, open(save_path, "wb") as f_dst:
                    f_dst.write(f_src.read())
                QMessageBox.information(self, "Saved", f"Image saved to:\n{save_path}")
            except Exception as e:
                QMessageBox.critical(self, "Save Failed", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RealESRGANGUI()
    window.show()
    sys.exit(app.exec())
