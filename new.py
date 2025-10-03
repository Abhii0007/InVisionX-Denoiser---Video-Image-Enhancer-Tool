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



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Paint-like Editor")

        layout = QVBoxLayout()
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Buttons
        open_btn = QPushButton("Open Image")
        pen_btn = QPushButton("Enable Pen")
        text_btn = QPushButton("Enable Text")
        save_btn = QPushButton("Save Image")
        undo_btn = QPushButton("Undo")


        layout.addWidget(open_btn)
        layout.addWidget(pen_btn)
        layout.addWidget(text_btn)
        layout.addWidget(save_btn)
        layout.addWidget(undo_btn)

        # Image Viewer
        self.viewer = ImageViewer()
        layout.addWidget(self.viewer)
        undo_btn.clicked.connect(self.viewer.undo) #----------------

        # Connections
        open_btn.clicked.connect(self.open_image)
        pen_btn.clicked.connect(self.toggle_pen)
        text_btn.clicked.connect(self.toggle_text)
        save_btn.clicked.connect(self.save_image)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
