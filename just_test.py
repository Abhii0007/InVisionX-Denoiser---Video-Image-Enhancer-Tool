# This Python file uses the following encoding: utf-8
import sys
import os
from datetime import datetime
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


from PySide6.QtGui import QPixmap, QWheelEvent, QMouseEvent, QPainter,QImage


from PySide6.QtCore import QObject, Signal
import subprocess
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
class UpscaleWorker(QObject):
    output_signal = Signal(str)
    finished = Signal(bool, str)  # success, error_message

    def __init__(self, exe_path, input_path, output_path, scale=2):
        super().__init__()
        self.exe_path = exe_path
        self.input_path = input_path
        self.output_path = output_path
        self.scale = scale
        self._process = None

    def run(self):
        cmd = [
            self.exe_path,
            "-i", self.input_path,
            "-o", self.output_path,
            "-n", "realesr-animevideov3",
            "-s", str(self.scale)
        ]

        try:
            self._process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )

            while True:
                line = self._process.stdout.readline()
                if line == '' and self._process.poll() is not None:
                    break
                if line:
                    self.output_signal.emit(line.rstrip())

            self._process.stdout.close()
            returncode = self._process.wait()

            if returncode == 0:
                self.finished.emit(True, "")
            else:
                self.finished.emit(False, f"Upscaling exited with code {returncode}")

        except Exception as e:
            self.finished.emit(False, str(e))

            
            

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget,
    QPushButton, QFileDialog, QGraphicsView, QGraphicsScene,
    QGraphicsPixmapItem, QGraphicsPathItem, QGraphicsTextItem, QInputDialog
)
from PySide6.QtGui import (
    QPixmap, QPainterPath, QWheelEvent, QMouseEvent, QPainter
)
from PySide6.QtCore import Qt

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog,
    QVBoxLayout, QWidget, QInputDialog
)
from PySide6.QtGui import QPixmap, QPainter, QPen, QColor, QFont
from PySide6.QtCore import Qt, QPoint
    
    
    
class ImageViewer(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setScene(QGraphicsScene(self))
        self.pixmap_item = QGraphicsPixmapItem()
        self.scene().addItem(self.pixmap_item)

        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.scale_factor = 1.0

        # Drawing state
        self.drawing = False
        self.path = None
        self.pen_enabled = False
        self.text_enabled = False

        # Undo stack
        self.items_stack = []

    def set_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.pixmap_item.setPixmap(pixmap)
        self.scene().setSceneRect(pixmap.rect())
        self.reset_transform()
        self.items_stack.clear()  # clear undo stack when new image is loaded

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

    def mousePressEvent(self, event: QMouseEvent):
        scene_pos = self.mapToScene(event.position().toPoint())
        if self.pen_enabled and event.button() == Qt.LeftButton:
            self.drawing = True
            self.path = QPainterPath(scene_pos)
            self.current_item = QGraphicsPathItem(self.path)
            self.current_item.setPen(QPen(Qt.red, 3))
            self.scene().addItem(self.current_item)
            self.items_stack.append(self.current_item)  # add to undo stack
        elif self.text_enabled and event.button() == Qt.LeftButton:
            text, ok = QInputDialog.getText(self, "Add Text", "Enter text:")
            if ok and text.strip():
                item = QGraphicsTextItem(text.strip())
                item.setDefaultTextColor(Qt.blue)
                item.setPos(scene_pos)
                self.scene().addItem(item)
                self.items_stack.append(item)  # add to undo stack
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.drawing and self.pen_enabled:
            scene_pos = self.mapToScene(event.position().toPoint())
            self.path.lineTo(scene_pos)
            self.current_item.setPath(self.path)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if self.drawing and self.pen_enabled and event.button() == Qt.LeftButton:
            self.drawing = False
        else:
            super().mouseReleaseEvent(event)

    def undo(self):
        if self.items_stack:
            last_item = self.items_stack.pop()
            self.scene().removeItem(last_item)
            del last_item

    def save_image(self, path):
        rect = self.scene().sceneRect()
        image = QPixmap(int(rect.width()), int(rect.height()))
        image.fill(Qt.white)
        painter = QPainter(image)
        self.scene().render(painter)
        painter.end()
        image.save(path)

        
from PySide6.QtWidgets import QTextEdit,QHBoxLayout
import re      
        
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence,QShortcut
   
import shutil
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog,
    QLabel, QProgressBar, QTextEdit, QMessageBox
)
from PySide6.QtCore import Qt, QThread, Signal
from concurrent.futures import ThreadPoolExecutor, as_completed
import multiprocessing
import threading     
# Video Upscaling Settings------------------start------------------------

class ExtractFramesWorker(QThread):
    progress = Signal(str)
    done = Signal(bool, str)

    def __init__(self, video_path, output_folder):
        super().__init__()
        self.video_path = video_path
        self.output_folder = output_folder
        self._abort = False
        self._process = None

    def abort(self):
        self._abort = True
        if self._process:
            self._process.terminate()

    def run(self):
        try:
            if os.path.exists(self.output_folder):
                shutil.rmtree(self.output_folder)
            os.makedirs(self.output_folder)

            cmd = [
                "ffmpeg", "-y", "-i", self.video_path,
                os.path.join(self.output_folder, "frame_%05d.png")
            ]
            self.progress.emit(f"Extracting frames from {self.video_path}...")
            self._process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

            for line in self._process.stdout:
                if self._abort:
                    self._process.terminate()
                    self.done.emit(False, "Extraction aborted by user.")
                    return
                self.progress.emit(line.strip())

            self._process.wait()
            if self._process.returncode == 0:
                self.done.emit(True, "")
            else:
                self.done.emit(False, f"ffmpeg exited with code {self._process.returncode}")
        except Exception as e:
            self.done.emit(False, str(e))


class UpscaleFramesWorker(QThread):
    progress = Signal(str)
    progress_count = Signal(int, int)
    done = Signal(bool, str)

    def __init__(self, realesrgan_path, input_folder, output_folder, scale):
        super().__init__()
        self.realesrgan_path = realesrgan_path
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.scale = scale
        self._abort = False
        self._lock = threading.Lock()
        self._processes = []

    def abort(self):
        """Request to cancel the operation."""
        self._abort = True
        for p in self._processes:
            try:
                p.terminate()
            except Exception:
                pass

    def upscale_one(self, input_path, output_path, img_name):
        """Run Real-ESRGAN for a single frame."""
        if self._abort:
            return False
        cmd = [
            self.realesrgan_path,
            "-i", input_path,
            "-o", output_path,
            "-n", "realesr-animevideov3",
            "-s", str(self.scale),
            "-g", "0"
        ]
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        self._processes.append(process)
        for line in process.stdout:
            if self._abort:
                process.terminate()
                return False
            line = line.strip()
            if line:
                self.progress.emit(f"{img_name}: {line}")
        process.wait()
        return process.returncode == 0

    def run(self):
        try:
            if os.path.exists(self.output_folder):
                shutil.rmtree(self.output_folder)
            os.makedirs(self.output_folder)

            images = sorted([
                f for f in os.listdir(self.input_folder)
                if f.lower().endswith(('.png', '.jpg', '.jpeg'))
            ])
            total = len(images)
            if total == 0:
                self.done.emit(False, "No frames found to upscale!")
                return

            self.progress.emit(f"Upscaling {total} frames (multi-threaded)...")

            max_concurrent_jobs = min(3, multiprocessing.cpu_count())
            completed = 0

            with ThreadPoolExecutor(max_workers=max_concurrent_jobs) as executor:
                futures = {}
                for img_name in images:
                    if self._abort:
                        self.done.emit(False, "Upscaling aborted by user.")
                        return
                    input_path = os.path.join(self.input_folder, img_name)
                    output_path = os.path.join(self.output_folder, img_name)
                    future = executor.submit(self.upscale_one, input_path, output_path, img_name)
                    futures[future] = img_name

                for future in as_completed(futures):
                    if self._abort:
                        self.done.emit(False, "Upscaling aborted by user.")
                        return
                    img = futures[future]
                    result = future.result()
                    with self._lock:
                        completed += 1
                    if not result and not self._abort:
                        self.done.emit(False, f"Upscaling failed at frame: {img}")
                        return
                    self.progress.emit(f"Upscaled frame {completed}/{total} ({img})")
                    self.progress_count.emit(completed, total)

            if not self._abort:
                self.done.emit(True, "")
            else:
                self.done.emit(False, "Upscaling aborted by user.")
        except Exception as e:
            self.done.emit(False, str(e))


class BuildVideoWorker(QThread):
    progress = Signal(str)
    done = Signal(bool, str)

    def __init__(self, frames_folder, output_video_path, fps):
        super().__init__()
        self.frames_folder = frames_folder
        self.output_video_path = output_video_path
        self.fps = fps
        self._abort = False
        self._process = None

    def abort(self):
        self._abort = True
        if self._process:
            self._process.terminate()

    def run(self):
        try:
            cmd = [
                "ffmpeg", "-y",
                "-r", str(self.fps),
                "-i", os.path.join(self.frames_folder, "frame_%05d.png"),
                "-c:v", "libx264",
                "-pix_fmt", "yuv420p",
                self.output_video_path
            ]
            self.progress.emit(f"Building video {self.output_video_path} ...")
            self._process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in self._process.stdout:
                if self._abort:
                    self._process.terminate()
                    self.done.emit(False, "Build aborted by user.")
                    return
                self.progress.emit(line.strip())
            self._process.wait()
            if self._process.returncode == 0:
                self.done.emit(True, "")
            else:
                self.done.emit(False, f"ffmpeg exited with code {self._process.returncode}")
        except Exception as e:
            self.done.emit(False, str(e))






# Video Upscalind---------------------END-------------------------
    
        
        
        
        
        
        

from window1 import Ui_MainWindow
class window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form = Ui_MainWindow()
        self.form.setupUi(self)
        
        
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        
        self.input_path = ""        
        self.output_path = os.path.join("Output_image", "last_output.png")
        
        
        
        
        
        
        self.image_viewer = ImageViewer()
        layout = QVBoxLayout(self.form.widget_image_preview)
        #self.image_viewer.setMinimumSize(300, 300)
        layout.addWidget(self.image_viewer)
        self.image_viewer.set_image(r"UI\a1.jpg")
        
        self.image_viewer_2 = ImageViewer()
        layout = QVBoxLayout(self.form.widget_image_output)
        #self.image_viewer.setMinimumSize(300, 300)
        layout.addWidget(self.image_viewer_2)
        self.image_viewer_2.set_image(r"UI\a2.jpg")

        
        
        
        
        self.form.toolButton_browse_image.clicked.connect(self.import_image)
        self.form.actionOpen.triggered.connect(self.import_image)
        
        self.form.pushButton_upscale_image.clicked.connect(self.convert_image)
        self.form.actionUpscale_Image.triggered.connect(self.convert_image)
        
        self.form.pushButton_save_as_image.clicked.connect(self.save_image)
        self.form.pushButton_save_image.clicked.connect(self.save_instant)
        self.form.actionsave.triggered.connect(self.save_image)
        
        self.form.actionExit.triggered.connect(QApplication.exit)
        
        self.form.toolButton_image_review.clicked.connect(self.window_image_viewer_preview)
        self.form.actionReview.triggered.connect(self.window_image_viewer_preview)
    
        self.form.toolButton_image_preview_open.clicked.connect(self.window_image_viewer_output)
        self.form.actionFullscreen_View.triggered.connect(self.window_image_viewer_output)
        
        self.form.pushButton_Send_to_input.clicked.connect(self.send_to_input)
        self.form.action_move_to_input.triggered.connect(self.send_to_input)
        self.form.toolButton_show_output_folder.clicked.connect(self.open_output_folder)
        self.form.toolButton_open_and_read_image.clicked.connect(self.load_image_with_metadata)
        
        
        
        
        shortcut_left = QShortcut(QKeySequence("Ctrl+,"), self)   # Ctrl + comma
        shortcut_left.activated.connect(self.move_left)

        shortcut_right = QShortcut(QKeySequence("Ctrl+."), self)  # Ctrl + period
        shortcut_right.activated.connect(self.move_right)







        # Video Upscaling Settings------------------start------------------------
        
        
        self.video_path = None
        self.frames_folder = "extracted_frames"
        self.upscaled_frames_folder = "upscaled_frames"
        self.output_video_path = "output_upscaled.mp4"
        self.realesrgan_exe = r"realesrgan\realesrgan-ncnn-vulkan.exe"
        self.fps = 30
        self.scale = 2

        # Disable everything except Select
        self.form.pushButton_extract_frames.setEnabled(False)
        self.form.pushButton_upscale_frames.setEnabled(False)
        self.form.pushButton_build_video.setEnabled(False)
        self.form.pushButton_Abort.setEnabled(False)
        
        
        self.form.toolButton_browse_video.clicked.connect(self.select_video)
        self.form.pushButton_extract_frames.clicked.connect(self.extract_frames)
        self.form.pushButton_upscale_frames.clicked.connect(self.upscale_frames)
        self.form.pushButton_build_video.clicked.connect(self.build_video)
        self.form.pushButton_Abort.clicked.connect(self.abort_processing)
        self.current_worker = None
        
        
        
        # Video Upscalind---------------------END-------------------------
    
    
    def load_image_with_metadata(self):
        # Open dialog to select image from Output_image
        folder = "Output_image"
        if not os.path.exists(folder):
            QMessageBox.warning(self, "Error", f"Folder '{folder}' does not exist!")
            return

        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Select Image", 
            folder, 
            "Images (*.png *.jpg *.jpeg)"
        )
        if not file_path:
            return  # user cancelled

        # Show image in image_viewer_2
        self.image_viewer_2.set_image(file_path)
        self.output_path = file_path  # Update output_path

        # Display image resolution
        image = QImage(file_path)
        if not image.isNull():
            self.form.label_image_output_preview.setText(
                f"Size : {image.width()} x {image.height()}"
            )

        # Look for corresponding text file in Output_image/metadata
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        metadata_folder = os.path.join(folder, "metadata")
        txt_file = os.path.join(metadata_folder, base_name + ".txt")

        if os.path.exists(txt_file):
            with open(txt_file, "r", encoding="utf-8") as f:
                text_content = f.read().strip()
                print("Metadata for selected image:")
                self.form.textEdit_image_metadata.setPlainText(text_content)
        else:
            print(f"No metadata file found for {base_name}")
            self.form.textEdit_image_metadata.setPlainText(f"No metadata found for {base_name}")
            

    def open_output_folder(self):
        current_dir = os.getcwd()
        folder_path = os.path.join(current_dir, "Output_image")

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        os.startfile(folder_path)

    def move_left(self):
        """Decrease slider value until it reaches 2"""
        if self.form.horizontalSlider_image_factor.value() > 2:
            self.form.horizontalSlider_image_factor.setValue(self.form.horizontalSlider_image_factor.value() - 1)

    def move_right(self):
        """Increase form.horizontalSlider_image_factor value until it reaches 4"""
        if self.form.horizontalSlider_image_factor.value() < 4:
            self.form.horizontalSlider_image_factor.setValue(self.form.horizontalSlider_image_factor.value() + 1)
    
    
    
    def window_image_viewer_output(self):
        global viewer_window
        viewer_window = window_image_viewer()
        
        
        viewer_window.viewer.set_image(self.output_path)
        viewer_window.show()
        
    def window_image_viewer_preview(self):
        global viewer_window
        viewer_window = window_image_viewer()
        
        
        viewer_window.viewer.set_image(self.input_path)
        viewer_window.show()
      

    def import_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Images (*.png *.jpg *.jpeg)"
        )
        if file_path:
            self.input_path = file_path
            self.form.lineEdit_pic_location.setText(file_path)
            self.image_viewer.set_image(file_path)

            # Load image to get resolution
            image = QImage(file_path)
            if not image.isNull():
                self.form.label_image_preview.setText(f"Size : {image.width()} x {image.height()}")
                #print(f"Image resolution: {image.width()} x {image.height()}")
        
    def send_to_input(self):
        file_path = self.output_path
        if file_path:
            self.input_path = file_path
            self.form.lineEdit_pic_location.setText(file_path)
            self.image_viewer.set_image(file_path)

            # Load image to get resolution
            image = QImage(file_path)
            if not image.isNull():
                self.form.label_image_preview.setText(f"Size : {image.width()} x {image.height()}")
                #print(f"Image resolution: {image.width()} x {image.height()}")



    def convert_image(self):
        self.form.progressBar.setValue(0)

        if not self.input_path:
            QMessageBox.warning(self, "Error", "Please import an image first.")
            return

        exe_path = os.path.join("realesrgan", "realesrgan-ncnn-vulkan.exe")
        if not os.path.exists(exe_path):
            QMessageBox.critical(self, "Error", f"{exe_path} not found.")
            return

        self.form.textEdit_console_output.clear()

       

        scale = self.form.horizontalSlider_image_factor.value()
        self.thread = QThread()
        self.worker = UpscaleWorker(exe_path, self.input_path, self.output_path, scale)
        self.worker.moveToThread(self.thread)

        # Connections
        self.worker.output_signal.connect(self.append_console_text)
        self.worker.finished.connect(self.on_worker_finished)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()


    def append_console_text(self, text):
        self.form.textEdit_console_output.append(text)
        scrollbar = self.form.textEdit_console_output.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

        match = re.match(r"^\s*(\d+(?:\.\d+)?)\s*%", text)
        if match:
            percent = float(match.group(1))
            self.form.progressBar.setValue(int(percent))


    def on_worker_finished(self, success, error_msg):
        # Step 1: close progress dialog
        if hasattr(self, "progress"):
            self.progress.close()

        # Step 2: Show success/fail message box
        if success:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Success")
            msg_box.setText("Image upscaled successfully.")
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.buttonClicked.connect(lambda _: self.on_upscale_done(success, error_msg))
            msg_box.exec()
        else:
            QMessageBox.critical(self, "Upscaling Failed", error_msg)
            # You can optionally call on_upscale_done(False, error_msg) immediately here


    def on_upscale_done(self, success, error_msg):
        # Step 3: update UI
        self.form.progressBar.setValue(100 if success else 0)

        if success and os.path.exists(self.output_path):
            self.image_viewer_2.set_image(self.output_path)
            image = QImage(self.output_path)
            if not image.isNull():
                self.form.label_image_output_preview.setText(
                    f"Size : {image.width()} x {image.height()}"
                )
   
    def save_instant(self):
        if not os.path.exists(self.output_path):
            QMessageBox.warning(self, "Error", "No converted image to save.")
            return

        # Ensure output folder exists
        folder = "Output_image"
        if not os.path.exists(folder):
            os.makedirs(folder)
            
        folder1 = r"Output_image\metadata"
        if not os.path.exists(folder1):
            os.makedirs(folder1)

        # Create timestamp-based unique name
        timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
        base_name = f"image_{timestamp}"

        # Save image
        image_path = os.path.join(folder, base_name + ".jpg")
        try:
            with open(self.output_path, "rb") as f_src, open(image_path, "wb") as f_dst:
                f_dst.write(f_src.read())
        except Exception as e:
            QMessageBox.critical(self, "Save Failed", f"Failed to save image:\n{str(e)}")
            return

        # Save text metadata
        text_content = self.form.textEdit_image_metadata.toPlainText().strip()
        text_path = os.path.join(folder1, base_name + ".txt")
        try:
            with open(text_path, "w", encoding="utf-8") as f:
                f.write(text_content)
        except Exception as e:
            QMessageBox.critical(self, "Save Failed", f"Failed to save metadata:\n{str(e)}")
            return

        # Confirmation message
        QMessageBox.information(
            self,
            "Saved",
            f"Image saved to:\n{image_path}\nMetadata saved to:\n{text_path}"
        )

                
    def save_image(self):
        if not os.path.exists(self.output_path):
            QMessageBox.warning(self, "Error", "No converted image to save.")
            return
        
        timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
        base_name = f"image_{timestamp}"
        
        save_path, _ = QFileDialog.getSaveFileName(self, "Save Image As", base_name, "PNG Files (*.png);;JPEG Files (*.jpg *.jpeg)")
        if save_path:
            try:
                with open(self.output_path, "rb") as f_src, open(save_path, "wb") as f_dst:
                    f_dst.write(f_src.read())
                QMessageBox.information(self, "Saved", f"Image saved to:\n{save_path}")
            except Exception as e:
                QMessageBox.critical(self, "Save Failed", str(e))
    
    
    # Video Upscaling Settings------------------start------------------------
            
    def log(self, text):
        self.form.textEdit_console_output.append(text)
        self.form.textEdit_console_output.ensureCursorVisible()

    def update_progress_bar(self, completed, total):
        self.form.progressBar.setMaximum(total)
        self.form.progressBar.setValue(completed)

    def select_video(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select Video", "", "Videos (*.mp4 *.avi *.mkv *.mov)")
        if file:
            self.video_path = file
            self.form.lineEdit_video_location.setText(f"Selected video: {file}")
            self.form.pushButton_extract_frames.setEnabled(True)
            self.form.pushButton_upscale_frames.setEnabled(False)
            self.form.pushButton_build_video.setEnabled(False)
            self.log(f"Video selected: {file}")

    def abort_processing(self):
        if self.current_worker:
            self.log("Aborting current task...")
            self.current_worker.abort()
            self.form.pushButton_Abort.setEnabled(False)

    def extract_frames(self):
        if not self.video_path:
            QMessageBox.warning(self, "Warning", "Select a video first!")
            return
        self.form.pushButton_extract_frames.setEnabled(False)
        self.form.pushButton_Abort.setEnabled(True)
        self.log("Starting frame extraction...")
        self.current_worker = ExtractFramesWorker(self.video_path, self.frames_folder)
        self.current_worker.progress.connect(self.log)
        self.current_worker.done.connect(self.on_extract_done)
        self.current_worker.start()

    def on_extract_done(self, success, error):
        self.form.pushButton_Abort.setEnabled(False)
        self.form.pushButton_extract_frames.setEnabled(True)
        if success:
            self.log("Frame extraction completed.")
            self.form.pushButton_upscale_frames.setEnabled(True)
        else:
            self.log(f"Extraction failed: {error}")

    def upscale_frames(self):
        if not os.path.exists(self.frames_folder):
            QMessageBox.warning(self, "Warning", "Extract frames first!")
            return
        self.form.pushButton_upscale_frames.setEnabled(False)
        self.form.pushButton_Abort.setEnabled(True)
        self.progress_bar.setValue(0)
        self.progress_bar.setMaximum(1)
        self.log("Starting frame upscaling...")
        self.current_worker = UpscaleFramesWorker(
            self.realesrgan_exe, self.frames_folder, self.upscaled_frames_folder, self.scale
        )
        self.current_worker.progress.connect(self.log)
        self.current_worker.progress_count.connect(self.update_progress_bar)
        self.current_worker.done.connect(self.on_upscale_done)
        self.current_worker.start()

    def on_upscale_done(self, success, error):
        self.form.pushButton_Abort.setEnabled(False)
        self.form.pushButton_upscale_frames.setEnabled(True)
        if success:
            self.log("Upscaling completed.")
            self.form.pushButton_build_video.setEnabled(True)
        else:
            self.log(f"Upscaling failed or aborted: {error}")

    def build_video(self):
        if not os.path.exists(self.upscaled_frames_folder):
            QMessageBox.warning(self, "Warning", "Upscale frames first!")
            return
        self.form.pushButton_build_video.setEnabled(False)
        self.form.pushButton_Abort.setEnabled(True)
        self.log("Starting video build...")
        self.current_worker = BuildVideoWorker(self.upscaled_frames_folder, self.output_video_path, self.fps)
        self.current_worker.progress.connect(self.log)
        self.current_worker.done.connect(self.on_build_done)
        self.current_worker.start()

    def on_build_done(self, success, error):
        self.form.pushButton_Abort.setEnabled(False)
        self.form.pushButton_build_video.setEnabled(True)
        if success:
            self.log(f"Video built successfully: {self.output_video_path}")
            QMessageBox.information(self, "Success", f"Saved: {self.output_video_path}")
        else:
            self.log(f"Build failed or aborted: {error}")
    # Video Upscaling Settings------------------End------------------------
     
                  
from window1_image_viewer import Ui_Form
class window_image_viewer(QMainWindow):
    def __init__(self, parent=None):
        
        super().__init__(parent)
        self.form_image = Ui_Form()
        self.form_image.setupUi(self)
        
        
        self.form_image.pushButton_open_image.clicked.connect(self.open_image)
        self.form_image.pushButton_Save_image.clicked.connect(self.save_image)
        self.form_image.pushButton_pen_tool.clicked.connect(self.toggle_pen)
        self.form_image.pushButton_add_text.clicked.connect(self.toggle_text)
        
        self.viewer = ImageViewer()
        self.form_image.pushButton_undo.clicked.connect(self.viewer.undo)
        self.showMaximized()
        
        layout = QVBoxLayout(self.form_image.widget_image_output)
        #self.viewer.setMinimumSize(300, 300)
        layout.addWidget(self.viewer)
        
        
        shortcut_undo = QShortcut(QKeySequence("Ctrl+z"), self)   # Ctrl + comma
        shortcut_undo.activated.connect(self.viewer.undo)
        
        
        
    def resizeEvent(self, event):
        """Resize widget_image_output to match window size"""
        self.form_image.widget_image_output.setGeometry(0, 0, self.width(), self.height())
        self.viewer.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)
        
        
    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.bmp)")
        if file_name:
            self.viewer.set_image(file_name)

    def toggle_pen(self):
        self.viewer.pen_enabled = not self.viewer.pen_enabled
        self.viewer.text_enabled = False  # disable text if pen is enabled

    def toggle_text(self):
        self.viewer.text_enabled = not self.viewer.text_enabled
        self.viewer.pen_enabled = False  # disable pen if text is enabled

    def save_image(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG (*.png);;JPG (*.jpg)")
        if file_name:
            self.viewer.save_image(file_name)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = window()
    widget.show()
    sys.exit(app.exec())