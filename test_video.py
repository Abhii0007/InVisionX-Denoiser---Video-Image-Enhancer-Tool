import sys
import os
import subprocess
import shutil
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog,
    QLabel, QProgressBar, QTextEdit, QMessageBox
)
from PySide6.QtCore import Qt, QThread, Signal

class ExtractFramesWorker(QThread):
    progress = Signal(str)
    done = Signal(bool, str)
    
    def __init__(self, video_path, output_folder):
        super().__init__()
        self.video_path = video_path
        self.output_folder = output_folder

    def run(self):
        try:
            # Create output folder (clear if exists)
            if os.path.exists(self.output_folder):
                shutil.rmtree(self.output_folder)
            os.makedirs(self.output_folder)

            # ffmpeg command to extract frames as PNG
            cmd = [
                "ffmpeg", "-y", "-i", self.video_path,
                os.path.join(self.output_folder, "frame_%05d.png")
            ]
            self.progress.emit(f"Extracting frames from {self.video_path}...")
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

            for line in process.stdout:
                self.progress.emit(line.strip())

            process.wait()
            if process.returncode == 0:
                self.done.emit(True, "")
            else:
                self.done.emit(False, f"ffmpeg exited with code {process.returncode}")
        except Exception as e:
            self.done.emit(False, str(e))


from concurrent.futures import ThreadPoolExecutor, as_completed
import multiprocessing

class UpscaleFramesWorker(QThread):
    progress = Signal(str)
    done = Signal(bool, str)

    def __init__(self, realesrgan_path, input_folder, output_folder, scale):
        super().__init__()
        self.realesrgan_path = realesrgan_path
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.scale = scale

    def upscale_one(self, input_path, output_path, img):
        """Run Real-ESRGAN on a single frame"""
        cmd = [
            self.realesrgan_path,
            "-i", input_path,
            "-o", output_path,
            "-n", "realesr-animevideov3",
            "-s", str(self.scale),
            "-g", "0"   # ensure GPU id is set
        ]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            self.progress.emit(f"{img}: {line.strip()}")
        process.wait()
        return process.returncode == 0

    def run(self):
        try:
            if os.path.exists(self.output_folder):
                shutil.rmtree(self.output_folder)
            os.makedirs(self.output_folder)

            images = sorted([f for f in os.listdir(self.input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
            total = len(images)
            if total == 0:
                self.done.emit(False, "No frames found to upscale!")
                return

            self.progress.emit(f"Upscaling {total} frames using multi-threading...")

            # Use all CPU cores (adjust if needed)
            max_workers = multiprocessing.cpu_count()

            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = []
                for img in images:
                    input_path = os.path.join(self.input_folder, img)
                    output_path = os.path.join(self.output_folder, img)
                    futures.append(executor.submit(self.upscale_one, input_path, output_path, img))

                completed = 0
                for future in as_completed(futures):
                    completed += 1
                    if not future.result():
                        self.done.emit(False, f"Upscaling failed on some frames")
                        return
                    self.progress.emit(f"Progress: {completed}/{total}")

            self.done.emit(True, "")
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

    def run(self):
        try:
            # ffmpeg command to build video from frames (assuming PNG)
            cmd = [
                "ffmpeg", "-y",
                "-r", str(self.fps),
                "-i", os.path.join(self.frames_folder, "frame_%05d.png"),
                "-c:v", "libx264",
                "-pix_fmt", "yuv420p",
                self.output_video_path
            ]
            self.progress.emit(f"Building video {self.output_video_path} ...")
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                self.progress.emit(line.strip())
            process.wait()
            if process.returncode == 0:
                self.done.emit(True, "")
            else:
                self.done.emit(False, f"ffmpeg exited with code {process.returncode}")
        except Exception as e:
            self.done.emit(False, str(e))


class VideoUpscalerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Upscaler with Real-ESRGAN")

        self.layout = QVBoxLayout(self)

        # Widgets
        self.video_path_label = QLabel("No video selected")
        self.select_video_btn = QPushButton("Select Video")
        self.extract_frames_btn = QPushButton("Extract Frames")
        self.upscale_frames_btn = QPushButton("Upscale Frames")
        self.build_video_btn = QPushButton("Build Video")
        self.progress_bar = QProgressBar()
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)

        self.layout.addWidget(self.video_path_label)
        self.layout.addWidget(self.select_video_btn)
        self.layout.addWidget(self.extract_frames_btn)
        self.layout.addWidget(self.upscale_frames_btn)
        self.layout.addWidget(self.build_video_btn)
        self.layout.addWidget(self.progress_bar)
        self.layout.addWidget(QLabel("Log Output:"))
        self.layout.addWidget(self.log_output)

        # State
        self.video_path = None
        self.frames_folder = "extracted_frames"
        self.upscaled_frames_folder = "upscaled_frames"
        self.output_video_path = "output_upscaled.mp4"
        self.realesrgan_exe = r"realesrgan\realesrgan-ncnn-vulkan.exe"  # Change if needed
        self.fps = 30  # default, will try to detect later
        self.scale = 2  # default upscale scale

        # Connections
        self.select_video_btn.clicked.connect(self.select_video)
        self.extract_frames_btn.clicked.connect(self.extract_frames)
        self.upscale_frames_btn.clicked.connect(self.upscale_frames)
        self.build_video_btn.clicked.connect(self.build_video)

        self.extract_frames_btn.setEnabled(False)
        self.upscale_frames_btn.setEnabled(False)
        self.build_video_btn.setEnabled(False)

    def log(self, text):
        self.log_output.append(text)
        self.log_output.ensureCursorVisible()

    def select_video(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select Video", "", "Videos (*.mp4 *.avi *.mkv *.mov)")
        if file:
            self.video_path = file
            self.video_path_label.setText(f"Selected video: {file}")
            self.extract_frames_btn.setEnabled(True)
            self.upscale_frames_btn.setEnabled(False)
            self.build_video_btn.setEnabled(False)
            self.log(f"Video selected: {file}")

            # Try to detect FPS with ffprobe (optional)
            try:
                import json
                result = subprocess.run(
                    ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                     "stream=r_frame_rate", "-of", "json", self.video_path],
                    capture_output=True, text=True
                )
                info = json.loads(result.stdout)
                if info and "streams" in info and len(info["streams"]) > 0:
                    rate = info["streams"][0]["r_frame_rate"]
                    num, den = rate.split('/')
                    self.fps = int(round(float(num) / float(den)))
                    self.log(f"Detected FPS: {self.fps}")
            except Exception as e:
                self.log(f"Could not detect FPS automatically, defaulting to 30: {e}")

    def extract_frames(self):
        if not self.video_path:
            QMessageBox.warning(self, "Warning", "Select a video first!")
            return
        self.extract_frames_btn.setEnabled(False)
        self.log("Starting frame extraction...")
        self.extract_worker = ExtractFramesWorker(self.video_path, self.frames_folder)
        self.extract_worker.progress.connect(self.log)
        self.extract_worker.done.connect(self.on_extract_done)
        self.extract_worker.start()

    def on_extract_done(self, success, error):
        self.extract_frames_btn.setEnabled(True)
        if success:
            self.log("Frame extraction completed.")
            self.upscale_frames_btn.setEnabled(True)
        else:
            self.log(f"Error extracting frames: {error}")
            QMessageBox.critical(self, "Error", f"Frame extraction failed:\n{error}")

    def upscale_frames(self):
        if not os.path.exists(self.frames_folder):
            QMessageBox.warning(self, "Warning", "Extract frames first!")
            return

        self.upscale_frames_btn.setEnabled(False)
        self.log("Starting frame upscaling...")
        # Here you can modify scale factor or add UI for it
        scale = self.scale

        self.upscale_worker = UpscaleFramesWorker(self.realesrgan_exe, self.frames_folder, self.upscaled_frames_folder, scale)
        self.upscale_worker.progress.connect(self.log)
        self.upscale_worker.done.connect(self.on_upscale_done)
        self.upscale_worker.start()

    def on_upscale_done(self, success, error):
        self.upscale_frames_btn.setEnabled(True)
        if success:
            self.log("Frame upscaling completed.")
            self.build_video_btn.setEnabled(True)
        else:
            self.log(f"Error upscaling frames: {error}")
            QMessageBox.critical(self, "Error", f"Upscaling failed:\n{error}")

    def build_video(self):
        if not os.path.exists(self.upscaled_frames_folder):
            QMessageBox.warning(self, "Warning", "Upscale frames first!")
            return
        self.build_video_btn.setEnabled(False)
        self.log("Starting video build...")
        self.build_worker = BuildVideoWorker(self.upscaled_frames_folder, self.output_video_path, self.fps)
        self.build_worker.progress.connect(self.log)
        self.build_worker.done.connect(self.on_build_done)
        self.build_worker.start()

    def on_build_done(self, success, error):
        self.build_video_btn.setEnabled(True)
        if success:
            self.log(f"Video built successfully: {self.output_video_path}")
            QMessageBox.information(self, "Success", f"Video saved as:\n{self.output_video_path}")
        else:
            self.log(f"Error building video: {error}")
            QMessageBox.critical(self, "Error", f"Video build failed:\n{error}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoUpscalerGUI()
    window.resize(600, 700)
    window.show()
    sys.exit(app.exec())
