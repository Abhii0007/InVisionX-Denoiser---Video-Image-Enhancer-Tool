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


from PySide6.QtGui import QPixmap, QWheelEvent, QMouseEvent, QPainter

class UpscaleWorker(QObject):
    finished = Signal(bool, str)  # success, error message

    def __init__(self, exe_path, input_path, output_path):
        super().__init__()
        self.exe_path = exe_path
        self.input_path = input_path
        self.output_path = output_path

    def run(self):
        cmd = [
            self.exe_path,
            "-i", self.input_path,
            "-o", self.output_path,
            "-n", "realesr-animevideov3",
            "-s", "2"
        ]
        try:
            subprocess.run(cmd, check=True)
            self.finished.emit(True, "")
        except subprocess.CalledProcessError as e:
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


class RealESRGANGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Real-ESRGAN Image Upscaler")
        self.setGeometry(100, 100, 800, 600)

        # Image viewer widget
        self.image_viewer = ImageViewer()

        # Buttons
        self.btn_import = QPushButton("Import Image")
        self.btn_convert = QPushButton("Convert Image")
        self.btn_save = QPushButton("Save Image")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_viewer)
        layout.addWidget(self.btn_import)
        layout.addWidget(self.btn_convert)
        layout.addWidget(self.btn_save)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # File paths
        self.input_path = ""
        self.output_path = os.path.join("realesrgan", "output.png")

        # Event bindings
        self.btn_import.clicked.connect(self.import_image)
        self.btn_convert.clicked.connect(self.convert_image)
        self.btn_save.clicked.connect(self.save_image)

    def import_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.input_path = file_path
            self.image_viewer.set_image(file_path)

    def convert_image(self):
        if not self.input_path:
            QMessageBox.warning(self, "Error", "Please import an image first.")
            return

        exe_path = os.path.join("realesrgan", "realesrgan-ncnn-vulkan.exe")
        if not os.path.exists(exe_path):
            QMessageBox.critical(self, "Error", f"{exe_path} not found.")
            return

        # Show progress dialog
        self.progress = QMessageBox(self)
        self.progress.setWindowTitle("Processing")
        self.progress.setText("Upscaling in progress...\nPlease wait.")
        self.progress.setStandardButtons(QMessageBox.NoButton)
        self.progress.show()

        # Start worker thread
        self.thread = QThread()
        self.worker = UpscaleWorker(exe_path, self.input_path, self.output_path)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.on_upscale_done)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()
        
    def on_upscale_done(self, success, error_msg):
        self.progress.hide()

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
