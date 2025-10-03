# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form1TvuRmk.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QTabWidget,
    QTextEdit, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 717)
        MainWindow.setMinimumSize(QSize(1080, 717))
        MainWindow.setMaximumSize(QSize(1080, 717))
        MainWindow.setStyleSheet(u"QToolTip {\n"
"   \n"
"    \n"
"    border: 1px solid #a0aec0;\n"
"    padding: 4px;\n"
"    border-radius: 6px;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionUpdate = QAction(MainWindow)
        self.actionUpdate.setObjectName(u"actionUpdate")
        self.action_move_to_input = QAction(MainWindow)
        self.action_move_to_input.setObjectName(u"action_move_to_input")
        self.actionFullscreen_View = QAction(MainWindow)
        self.actionFullscreen_View.setObjectName(u"actionFullscreen_View")
        self.actionReview = QAction(MainWindow)
        self.actionReview.setObjectName(u"actionReview")
        self.actionUpscale_Image = QAction(MainWindow)
        self.actionUpscale_Image.setObjectName(u"actionUpscale_Image")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 1100, 730))
        self.widget_2.setStyleSheet(u"background-color: rgb(165, 187, 230);")
        self.tabWidget = QTabWidget(self.widget_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 10, 1070, 675))
        self.tabWidget.setStyleSheet(u"#tabWidget::pane {\n"
"	background-color: rgb(78, 89, 109);\n"
"   \n"
"   \n"
"}\n"
"\n"
"#tabWidget QTabBar::tab {\n"
"    background-color: #66779e; /* Dark Blue */\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 3px 18px;\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"    margin-left: 10px;\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"#tabWidget QTabBar::tab:selected {\n"
"    background: #e4ebf8; /* Light Green */\n"
"    color: black;\n"
"    border: 1px solid #e4ebf8;\n"
"    border-bottom-color: #e4ebf8;\n"
"}\n"
"\n"
"#tabWidget QTabBar::tab:hover {\n"
"    background: #7c9bf1; /* Slightly lighter blue on hover */\n"
"    \n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.widget_12 = QWidget(self.tab)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(10, 0, 1061, 635))
        self.widget_12.setStyleSheet(u"#widget_12 {\n"
"    background-color: rgb(228, 235, 248);\n"
"\n"
"    border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 8px; /* Rounded */\n"
"}\n"
"")
        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(21, 60, 501, 504))
        self.widget_13.setStyleSheet(u"background-color: rgb(196, 208, 232);\n"
"    border-radius: 12px;")
        self.lineEdit_pic_location = QLineEdit(self.widget_13)
        self.lineEdit_pic_location.setObjectName(u"lineEdit_pic_location")
        self.lineEdit_pic_location.setGeometry(QRect(10, 60, 481, 41))
        self.lineEdit_pic_location.setStyleSheet(u"#lineEdit_pic_location {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font: 12pt \"Cambria\";\n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"\n"
"}\n"
"\n"
"#lineEdit_pic_location:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"#lineEdit_pic_location:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}\n"
"")
        self.lineEdit_pic_location.setReadOnly(True)
        self.label_5 = QLabel(self.widget_13)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(12, 17, 211, 31))
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(63, 74, 98);")
        self.label_9 = QLabel(self.widget_13)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(12, 120, 211, 31))
        font1 = QFont()
        font1.setFamilies([u"Cambria"])
        font1.setPointSize(16)
        self.label_9.setFont(font1)
        self.widget_image_preview = QWidget(self.widget_13)
        self.widget_image_preview.setObjectName(u"widget_image_preview")
        self.widget_image_preview.setGeometry(QRect(10, 160, 481, 290))
        self.widget_image_preview.setStyleSheet(u"background-color: rgb(228, 235, 248);\n"
"\n"
"    border: 1px solid #7986ac;\n"
"    border-radius: 8px;")
        self.toolButton_browse_image = QToolButton(self.widget_13)
        self.toolButton_browse_image.setObjectName(u"toolButton_browse_image")
        self.toolButton_browse_image.setGeometry(QRect(359, 15, 131, 30))
        font2 = QFont()
        font2.setPointSize(12)
        self.toolButton_browse_image.setFont(font2)
        self.toolButton_browse_image.setStyleSheet(u"background-color: rgb(228, 235, 248);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"    border: 1px solid #7986ac;\n"
"    border-radius: 4px;")
        self.horizontalSlider_image_factor = QSlider(self.widget_13)
        self.horizontalSlider_image_factor.setObjectName(u"horizontalSlider_image_factor")
        self.horizontalSlider_image_factor.setGeometry(QRect(316, 456, 160, 22))
        self.horizontalSlider_image_factor.setStyleSheet(u"#horizontalSlider_image_factor {\n"
"    min-height: 20px;\n"
"    border: none;\n"
"	background-color: #c4d0e8;\n"
"}\n"
"\n"
"/* Groove (track background) */\n"
"#horizontalSlider_image_factor::groove:horizontal {\n"
"    border: 1px solid #7986ac;       /* Matches your widget borders */\n"
"    height: 6px;\n"
"    background: #e4ebf8;             /* Same pastel as panels */\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"/* Handle (draggable knob) */\n"
"#horizontalSlider_image_factor::handle:horizontal {\n"
"    background: #7a8cb5;             /* Muted blue knob */\n"
"    border: 1px solid #5d6b8d;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -6px 0;                  /* Centers on groove */\n"
"    border-radius: 8px;              /* Round */\n"
"    \n"
"}\n"
"\n"
"/* Hover effect */\n"
"#horizontalSlider_image_factor::handle:horizontal:hover {\n"
"    background: #6a7baa;             /* Slightly lighter blue */\n"
"}\n"
"\n"
"/* Pressed (dragging) */\n"
"#horizontalSlider_image_factor::handle"
                        ":horizontal:pressed {\n"
"    background: #8ae6c3;             /* Soft green accent like focus state */\n"
"    border: 1px solid #5bb598;\n"
"}\n"
"\n"
"/* Filled portion (left of knob) */\n"
"#horizontalSlider_image_factor::sub-page:horizontal {\n"
"    background: #a5bbe6;             /* Light pastel blue fill */\n"
"    border: 1px solid #7986ac;\n"
"    height: 6px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"/* Remaining portion (right of knob) */\n"
"#horizontalSlider_image_factor::add-page:horizontal {\n"
"    background: #f4f6fb;             /* Very light gray-blue */\n"
"    border: 1px solid #a3b1d3;\n"
"    height: 6px;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.horizontalSlider_image_factor.setMinimum(2)
        self.horizontalSlider_image_factor.setMaximum(4)
        self.horizontalSlider_image_factor.setPageStep(1)
        self.horizontalSlider_image_factor.setValue(2)
        self.horizontalSlider_image_factor.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_image_factor.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.label_15 = QLabel(self.widget_13)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(180, 455, 134, 26))
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"color: rgb(63, 74, 98);")
        self.toolButton_image_review = QToolButton(self.widget_13)
        self.toolButton_image_review.setObjectName(u"toolButton_image_review")
        self.toolButton_image_review.setGeometry(QRect(399, 115, 91, 30))
        self.toolButton_image_review.setFont(font2)
        self.toolButton_image_review.setStyleSheet(u"background-color: rgb(228, 235, 248);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"    border: 1px solid #7986ac;\n"
"    border-radius: 4px;")
        self.label_16 = QLabel(self.widget_13)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(316, 476, 171, 26))
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"color: rgb(63, 74, 98);")
        self.label_image_preview = QLabel(self.widget_13)
        self.label_image_preview.setObjectName(u"label_image_preview")
        self.label_image_preview.setGeometry(QRect(10, 456, 161, 26))
        self.label_image_preview.setFont(font)
        self.label_image_preview.setStyleSheet(u"color: rgb(63, 74, 98);")
        self.label_image_preview.setLineWidth(2)
        self.widget_image_preview.raise_()
        self.lineEdit_pic_location.raise_()
        self.label_5.raise_()
        self.label_9.raise_()
        self.toolButton_browse_image.raise_()
        self.horizontalSlider_image_factor.raise_()
        self.label_15.raise_()
        self.toolButton_image_review.raise_()
        self.label_16.raise_()
        self.label_image_preview.raise_()
        self.pushButton_upscale_image = QPushButton(self.widget_12)
        self.pushButton_upscale_image.setObjectName(u"pushButton_upscale_image")
        self.pushButton_upscale_image.setGeometry(QRect(21, 575, 501, 41))
        font3 = QFont()
        font3.setFamilies([u"Cambria"])
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setItalic(False)
        self.pushButton_upscale_image.setFont(font3)
        self.pushButton_upscale_image.setStyleSheet(u"\n"
"#pushButton_upscale_image{\n"
"    color: #ffffff;\n"
"    background-color: #488dfa;\n"
"    \n"
"	font: 16pt \"Cambria\";\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"#pushButton_upscale_image:hover {\n"
"    background-color: #5478c7;\n"
"}\n"
"\n"
"#pushButton_upscale_image:pressed {\n"
"    background-color: #204070;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"color: rgb(255,255,255);\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_btn_select_image_4:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.label_10 = QLabel(self.widget_12)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(27, 24, 131, 25))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(84, 99, 130);\n"
"background-color: rgb(228, 235, 248);")
        self.widget_15 = QWidget(self.widget_12)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setGeometry(QRect(537, 60, 501, 566))
        self.widget_15.setStyleSheet(u"\n"
"background-color: rgb(183, 208, 255);\n"
"background-color: rgb(203, 221, 255);\n"
"    border-radius: 12px;")
        self.label_11 = QLabel(self.widget_15)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(12, 17, 211, 31))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgb(63, 74, 98);")
        self.widget_image_output = QWidget(self.widget_15)
        self.widget_image_output.setObjectName(u"widget_image_output")
        self.widget_image_output.setGeometry(QRect(10, 160, 481, 290))
        self.widget_image_output.setStyleSheet(u"background-color: rgb(66, 79, 117);\n"
"    border: 2px solid #a5bbe6;\n"
"    border-radius: 8px;")
        self.toolButton_image_preview_open = QToolButton(self.widget_15)
        self.toolButton_image_preview_open.setObjectName(u"toolButton_image_preview_open")
        self.toolButton_image_preview_open.setGeometry(QRect(359, 15, 131, 30))
        self.toolButton_image_preview_open.setFont(font2)
        self.toolButton_image_preview_open.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"    border: 1px solid #7986ac;\n"
"    border-radius: 4px;")
        self.pushButton_save_as_image = QPushButton(self.widget_15)
        self.pushButton_save_as_image.setObjectName(u"pushButton_save_as_image")
        self.pushButton_save_as_image.setGeometry(QRect(259, 514, 231, 41))
        self.pushButton_save_as_image.setFont(font3)
        self.pushButton_save_as_image.setStyleSheet(u"#pushButton_save_as_image{\n"
"    color: #ffffff;\n"
"    background-color: #3162ab;\n"
"    \n"
"	font: 16pt \"Cambria\";\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"#pushButton_save_as_image:hover {\n"
"    background-color: #5478c7;\n"
"}\n"
"\n"
"#pushButton_save_as_image:pressed {\n"
"    background-color: #204070;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"color: rgb(255,255,255);\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_save_as_image:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.textEdit_image_metadata = QTextEdit(self.widget_15)
        self.textEdit_image_metadata.setObjectName(u"textEdit_image_metadata")
        self.textEdit_image_metadata.setGeometry(QRect(10, 60, 481, 90))
        self.textEdit_image_metadata.setFont(font)
        self.textEdit_image_metadata.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"\n"
"    border: 1px solid #7986ac;\n"
"    border-radius: 8px;")
        self.pushButton_Send_to_input = QPushButton(self.widget_15)
        self.pushButton_Send_to_input.setObjectName(u"pushButton_Send_to_input")
        self.pushButton_Send_to_input.setGeometry(QRect(246, 460, 241, 41))
        self.pushButton_Send_to_input.setFont(font3)
        self.pushButton_Send_to_input.setStyleSheet(u"#pushButton_Send_to_input{\n"
"    color: #ffffff;\n"
"    background-color: #488dfa;\n"
"    \n"
"	font: 16pt \"Cambria\";\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"#pushButton_Send_to_input:hover {\n"
"    background-color: #5478c7;\n"
"}\n"
"\n"
"#pushButton_Send_to_input:pressed {\n"
"    background-color: #204070;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"color: rgb(255,255,255);\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_Send_to_input:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.label_image_output_preview = QLabel(self.widget_15)
        self.label_image_output_preview.setObjectName(u"label_image_output_preview")
        self.label_image_output_preview.setGeometry(QRect(10, 456, 161, 26))
        self.label_image_output_preview.setFont(font)
        self.label_image_output_preview.setStyleSheet(u"color: rgb(63, 74, 98);")
        self.label_image_output_preview.setLineWidth(2)
        self.pushButton_save_image = QPushButton(self.widget_15)
        self.pushButton_save_image.setObjectName(u"pushButton_save_image")
        self.pushButton_save_image.setGeometry(QRect(11, 514, 237, 41))
        self.pushButton_save_image.setFont(font3)
        self.pushButton_save_image.setStyleSheet(u"#pushButton_save_image{\n"
"    color: #ffffff;\n"
"    background-color: #8ba6ff;\n"
"    \n"
"	font: 16pt \"Cambria\";\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"#pushButton_save_image:hover {\n"
"    background-color: #5478c7;\n"
"}\n"
"\n"
"#pushButton_save_image:pressed {\n"
"    background-color: #204070;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"color: rgb(255,255,255);\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_save_image:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.toolButton_open_and_read_image = QToolButton(self.widget_15)
        self.toolButton_open_and_read_image.setObjectName(u"toolButton_open_and_read_image")
        self.toolButton_open_and_read_image.setGeometry(QRect(179, 15, 168, 30))
        self.toolButton_open_and_read_image.setFont(font2)
        self.toolButton_open_and_read_image.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"    border: 1px solid #7986ac;\n"
"    border-radius: 4px;")
        self.widget_image_output.raise_()
        self.label_11.raise_()
        self.toolButton_image_preview_open.raise_()
        self.pushButton_save_as_image.raise_()
        self.textEdit_image_metadata.raise_()
        self.pushButton_Send_to_input.raise_()
        self.label_image_output_preview.raise_()
        self.pushButton_save_image.raise_()
        self.toolButton_open_and_read_image.raise_()
        self.label_17 = QLabel(self.widget_12)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(541, 24, 140, 25))
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"color: rgb(84, 99, 130);\n"
"background-color: rgb(228, 235, 248);")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.widget_7 = QWidget(self.tab_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(10, 0, 1061, 635))
        self.widget_7.setStyleSheet(u"#widget_7 {\n"
"    background-color: rgb(228, 235, 248);\n"
"\n"
"    border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 8px; /* Rounded */\n"
"}\n"
"")
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(21, 60, 501, 504))
        self.widget_8.setStyleSheet(u"\n"
"background-color: rgb(183, 208, 255);\n"
"background-color: rgb(203, 221, 255);\n"
"    border-radius: 12px;")
        self.lineEdit_video_location = QLineEdit(self.widget_8)
        self.lineEdit_video_location.setObjectName(u"lineEdit_video_location")
        self.lineEdit_video_location.setGeometry(QRect(10, 52, 481, 41))
        self.lineEdit_video_location.setStyleSheet(u"#lineEdit_video_location {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font: 12pt \"Cambria\";\n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"  \n"
"}\n"
"\n"
"#lineEdit_video_location:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"#lineEdit_video_location:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}\n"
"")
        self.lineEdit_video_location.setReadOnly(True)
        self.label_4 = QLabel(self.widget_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(12, 15, 211, 31))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(84, 99, 130);\n"
"")
        self.label_6 = QLabel(self.widget_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(12, 93, 211, 31))
        self.label_6.setFont(font1)
        self.widget_video_preview = QWidget(self.widget_8)
        self.widget_video_preview.setObjectName(u"widget_video_preview")
        self.widget_video_preview.setGeometry(QRect(10, 125, 481, 225))
        self.widget_video_preview.setStyleSheet(u"background-color: rgb(244, 246, 251);\n"
"    border: 1px solid #7986ac;\n"
"    border-radius: 8px;")
        self.toolButton_browse_video = QToolButton(self.widget_8)
        self.toolButton_browse_video.setObjectName(u"toolButton_browse_video")
        self.toolButton_browse_video.setGeometry(QRect(258, 12, 131, 30))
        self.toolButton_browse_video.setFont(font2)
        self.toolButton_browse_video.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"    border: 1px solid #7986ac;\n"
"    border-radius: 4px;")
        self.horizontalSlider_video_factor = QSlider(self.widget_8)
        self.horizontalSlider_video_factor.setObjectName(u"horizontalSlider_video_factor")
        self.horizontalSlider_video_factor.setGeometry(QRect(326, 400, 160, 22))
        self.horizontalSlider_video_factor.setStyleSheet(u"#horizontalSlider_video_factor{\n"
"    min-height: 20px;\n"
"    border: none;\n"
"	background-color: #cbddff;\n"
"}\n"
"\n"
"/* Groove (track background) */\n"
"#horizontalSlider_video_factor::groove:horizontal {\n"
"    border: 1px solid #7986ac;       /* Matches your widget borders */\n"
"    height: 6px;\n"
"    background: #e4ebf8;             /* Same pastel as panels */\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"/* Handle (draggable knob) */\n"
"#horizontalSlider_video_factor::handle:horizontal {\n"
"    background: #7a8cb5;             /* Muted blue knob */\n"
"    border: 1px solid #5d6b8d;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -6px 0;                  /* Centers on groove */\n"
"    border-radius: 8px;              /* Round */\n"
"   \n"
"}\n"
"\n"
"/* Hover effect */\n"
"#horizontalSlider_video_factor::handle:horizontal:hover {\n"
"    background: #6a7baa;             /* Slightly lighter blue */\n"
"}\n"
"\n"
"/* Pressed (dragging) */\n"
"#horizontalSlider_video_factor::handle:h"
                        "orizontal:pressed {\n"
"    background: #8ae6c3;             /* Soft green accent like focus state */\n"
"    border: 1px solid #5bb598;\n"
"}\n"
"\n"
"/* Filled portion (left of knob) */\n"
"#horizontalSlider_video_factor::sub-page:horizontal {\n"
"    background: #a5bbe6;             /* Light pastel blue fill */\n"
"    border: 1px solid #7986ac;\n"
"    height: 6px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"/* Remaining portion (right of knob) */\n"
"#horizontalSlider_video_factor::add-page:horizontal {\n"
"    background: #f4f6fb;             /* Very light gray-blue */\n"
"    border: 1px solid #a3b1d3;\n"
"    height: 6px;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.horizontalSlider_video_factor.setMinimum(2)
        self.horizontalSlider_video_factor.setMaximum(4)
        self.horizontalSlider_video_factor.setPageStep(1)
        self.horizontalSlider_video_factor.setValue(2)
        self.horizontalSlider_video_factor.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_video_factor.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.label_12 = QLabel(self.widget_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(240, 396, 81, 26))
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: rgb(84, 99, 130);")
        self.toolButton_video_review = QToolButton(self.widget_8)
        self.toolButton_video_review.setObjectName(u"toolButton_video_review")
        self.toolButton_video_review.setGeometry(QRect(399, 12, 91, 30))
        self.toolButton_video_review.setFont(font2)
        self.toolButton_video_review.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"    border: 1px solid #7986ac;\n"
"    border-radius: 4px;")
        self.label_13 = QLabel(self.widget_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(326, 420, 171, 26))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: rgb(84, 99, 130);")
        self.pushButton_extract_frames = QPushButton(self.widget_8)
        self.pushButton_extract_frames.setObjectName(u"pushButton_extract_frames")
        self.pushButton_extract_frames.setGeometry(QRect(10, 400, 218, 41))
        self.pushButton_extract_frames.setFont(font3)
        self.pushButton_extract_frames.setStyleSheet(u"#pushButton_extract_frames{\n"
"	background-color: #92a5fa;\n"
"    color: #ffffff;\n"
"\n"
"    \n"
"	font: 16pt \"Cambria\";\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#pushButton_extract_frames:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.pushButton_upscale_frames = QPushButton(self.widget_8)
        self.pushButton_upscale_frames.setObjectName(u"pushButton_upscale_frames")
        self.pushButton_upscale_frames.setGeometry(QRect(10, 450, 218, 41))
        self.pushButton_upscale_frames.setFont(font3)
        self.pushButton_upscale_frames.setStyleSheet(u"#pushButton_upscale_frames{\n"
"	background-color: #92a5fa;\n"
"    color: #ffffff;\n"
"\n"
"    \n"
"	font: 16pt \"Cambria\";\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"#pushButton_upscale_frames:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.pushButton_Abort = QPushButton(self.widget_8)
        self.pushButton_Abort.setObjectName(u"pushButton_Abort")
        self.pushButton_Abort.setGeometry(QRect(359, 451, 131, 41))
        self.pushButton_Abort.setFont(font3)
        self.pushButton_Abort.setStyleSheet(u"#pushButton_Abort{\n"
"    color: #ffffff;\n"
"    background-color: #ff94a8;\n"
"    \n"
"	font: 16pt \"Cambria\";\n"
"    border: 2px solid #ff6164;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"#pushButton_Abort:hover {\n"
"    background-color: #ff6164;\n"
"}\n"
"\n"
"#pushButton_Abort:pressed {\n"
"    background-color: #cb4a4c;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"color: rgb(255,255,255);\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_Abort:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"   border: 2px solid rgb(180, 180, 180);\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.checkBox = QCheckBox(self.widget_8)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(200, 412, 31, 20))
        self.checkBox.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(144, 168, 255,0);")
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)
        self.checkBox_2 = QCheckBox(self.widget_8)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(200, 460, 31, 20))
        self.checkBox_2.setStyleSheet(u"background-color: rgba(106, 137, 202,0);\n"
"color: rgb(0, 0, 0);")
        self.checkBox_2.setCheckable(True)
        self.label_18 = QLabel(self.widget_8)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(241, 421, 51, 21))
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(u"color: rgb(84, 99, 130);")
        self.horizontalSlider_video = QSlider(self.widget_8)
        self.horizontalSlider_video.setObjectName(u"horizontalSlider_video")
        self.horizontalSlider_video.setGeometry(QRect(104, 363, 383, 22))
        self.horizontalSlider_video.setStyleSheet(u"")
        self.horizontalSlider_video.setOrientation(Qt.Orientation.Horizontal)
        self.pushlButton_video_play = QPushButton(self.widget_8)
        self.pushlButton_video_play.setObjectName(u"pushlButton_video_play")
        self.pushlButton_video_play.setGeometry(QRect(10, 359, 81, 32))
        self.pushlButton_video_play.setFont(font3)
        self.pushlButton_video_play.setStyleSheet(u"#pushlButton_video_play{\n"
"    color: #000000;\n"
"    background-color: #f7f7f7;\n"
"    \n"
"	font: 16pt \"Cambria\";\n"
"    border: 2px solid #92a5fa;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"#pushlButton_video_play:hover {\n"
"    background-color: #6a98fa;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#pushlButton_video_play:pressed {\n"
"    \n"
"	background-color: rgb(69, 100, 162);\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"color: rgb(255,255,255);\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushlButton_video_play:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"   border: 2px solid rgb(180, 180, 180);\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.label_7 = QLabel(self.widget_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(27, 24, 131, 25))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: rgb(63, 74, 98);\n"
"background-color: rgb(228, 235, 248);")
        self.widget_10 = QWidget(self.widget_7)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(537, 60, 501, 566))
        self.widget_10.setStyleSheet(u"background-color: rgb(196, 208, 232);\n"
"    border-radius: 12px;")
        self.label_8 = QLabel(self.widget_10)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(12, 17, 211, 31))
        self.label_8.setFont(font1)
        self.widget_video_output = QWidget(self.widget_10)
        self.widget_video_output.setObjectName(u"widget_video_output")
        self.widget_video_output.setGeometry(QRect(10, 57, 481, 225))
        self.widget_video_output.setStyleSheet(u"background-color: rgb(102, 119, 158);\n"
"    border: 2px solid #a5bbe6;\n"
"    border-radius: 8px;")
        self.toolButton_video_output_view = QToolButton(self.widget_10)
        self.toolButton_video_output_view.setObjectName(u"toolButton_video_output_view")
        self.toolButton_video_output_view.setGeometry(QRect(399, 15, 91, 30))
        self.toolButton_video_output_view.setFont(font2)
        self.toolButton_video_output_view.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"    border: 1px solid #7986ac;\n"
"    border-radius: 4px;")
        self.textEdit_video_metadata = QTextEdit(self.widget_10)
        self.textEdit_video_metadata.setObjectName(u"textEdit_video_metadata")
        self.textEdit_video_metadata.setGeometry(QRect(10, 332, 481, 170))
        self.textEdit_video_metadata.setFont(font)
        self.textEdit_video_metadata.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"\n"
"    border: 1px solid #7986ac;\n"
"    border-radius: 8px;")
        self.pushButton_save_video_with_metadata = QPushButton(self.widget_10)
        self.pushButton_save_video_with_metadata.setObjectName(u"pushButton_save_video_with_metadata")
        self.pushButton_save_video_with_metadata.setGeometry(QRect(11, 513, 480, 41))
        self.pushButton_save_video_with_metadata.setFont(font3)
        self.pushButton_save_video_with_metadata.setStyleSheet(u"\n"
"#pushButton_save_video_with_metadata{\n"
"    color: #ffffff;\n"
"    background-color: #a2a8fa;\n"
"    \n"
"	font: 16pt \"Cambria\";\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"#pushButton_save_video_with_metadata:hover {\n"
"    background-color: #5478c7;\n"
"}\n"
"\n"
"#pushButton_save_video_with_metadata:pressed {\n"
"    background-color: #204070;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"color: rgb(255,255,255);\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_save_video_with_metadata:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.toolButton_open_and_read_video = QToolButton(self.widget_10)
        self.toolButton_open_and_read_video.setObjectName(u"toolButton_open_and_read_video")
        self.toolButton_open_and_read_video.setGeometry(QRect(210, 15, 171, 30))
        self.toolButton_open_and_read_video.setFont(font2)
        self.toolButton_open_and_read_video.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"    border: 1px solid #7986ac;\n"
"    border-radius: 4px;")
        self.horizontalSlider_video_2 = QSlider(self.widget_10)
        self.horizontalSlider_video_2.setObjectName(u"horizontalSlider_video_2")
        self.horizontalSlider_video_2.setGeometry(QRect(103, 294, 383, 22))
        self.horizontalSlider_video_2.setStyleSheet(u"")
        self.horizontalSlider_video_2.setOrientation(Qt.Orientation.Horizontal)
        self.pushlButton_video_play_2 = QPushButton(self.widget_10)
        self.pushlButton_video_play_2.setObjectName(u"pushlButton_video_play_2")
        self.pushlButton_video_play_2.setGeometry(QRect(11, 290, 81, 32))
        self.pushlButton_video_play_2.setFont(font3)
        self.pushlButton_video_play_2.setStyleSheet(u"#pushlButton_video_play_2{\n"
"    color: #000000;\n"
"    background-color: #f7f7f7;\n"
"    \n"
"	font: 16pt \"Cambria\";\n"
"    border: 2px solid #92a5fa;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"#pushlButton_video_play_2:hover {\n"
"    background-color: #6a98fa;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#pushlButton_video_play_2:pressed {\n"
"    \n"
"	background-color: rgb(69, 100, 162);\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"color: rgb(255,255,255);\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushlButton_video_play_2:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"   border: 2px solid rgb(180, 180, 180);\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.label_14 = QLabel(self.widget_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(541, 24, 140, 25))
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"color: rgb(63, 74, 98);\n"
"background-color: rgb(228, 235, 248);")
        self.pushButton_start_upscaling_video = QPushButton(self.widget_7)
        self.pushButton_start_upscaling_video.setObjectName(u"pushButton_start_upscaling_video")
        self.pushButton_start_upscaling_video.setGeometry(QRect(22, 573, 501, 41))
        self.pushButton_start_upscaling_video.setFont(font3)
        self.pushButton_start_upscaling_video.setStyleSheet(u"#pushButton_start_upscaling_video{\n"
"    color: #ffffff;\n"
"    background-color: #6a98fa;\n"
"    \n"
"	font: 16pt \"Cambria\";\n"
"    border: 2px solid #488dfa;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#pushButton_start_upscaling_video:hover {\n"
"    background-color: #488dfa;\n"
"}\n"
"\n"
"#pushButton_start_upscaling_video:pressed {\n"
"    background-color: #204070;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"color: rgb(255,255,255);\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_start_upscaling_video:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.textEdit_console_output = QTextEdit(self.tab_3)
        self.textEdit_console_output.setObjectName(u"textEdit_console_output")
        self.textEdit_console_output.setGeometry(QRect(10, 0, 1061, 635))
        self.textEdit_console_output.setStyleSheet(u"#textEdit_console_output {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font: 12pt \"Cambria\";\n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"\n"
"}\n"
"\n"
"#textEdit_console_output:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"#textEdit_console_output:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}\n"
"")
        self.textEdit_console_output.setReadOnly(True)
        self.tabWidget.addTab(self.tab_3, "")
        self.toolButton_show_output_folder = QToolButton(self.widget_2)
        self.toolButton_show_output_folder.setObjectName(u"toolButton_show_output_folder")
        self.toolButton_show_output_folder.setGeometry(QRect(910, 54, 121, 30))
        self.toolButton_show_output_folder.setFont(font2)
        self.toolButton_show_output_folder.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"    border: 1px solid #7986ac;\n"
"    border-radius: 4px;")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(460, 10, 191, 20))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #9ca9c9;\n"
"    border-radius: 8px;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #d8ddef,\n"
"        stop:1 #c2c9dd\n"
"    );\n"
"    color: #2c3e50;\n"
"    text-align: center;\n"
"    font: bold 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 6px;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #5b8def,\n"
"        stop:1 #2a5dca\n"
"    );\n"
"    margin: 2px; /* gap inside */\n"
"}\n"
"")
        self.progressBar.setValue(0)
        self.label_status = QLabel(self.centralwidget)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(660, 7, 411, 25))
        self.label_status.setFont(font)
        self.label_status.setStyleSheet(u"color: rgb(84, 99, 130);\n"
"background-color: rgba(228, 235, 248,0);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1080, 33))
        self.menubar.setStyleSheet(u"QMenuBar {\n"
"    background-color: #7a8cb5;   /* Matches top frame */\n"
"    color: #ffffff;\n"
"    font: 11pt \"Segoe UI\";\n"
"    padding: 0px 4px;\n"
"    border-bottom: 1px solid #5d6b8d; /* Subtle divider */\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background: transparent;\n"
"    padding: 4px 12px;\n"
"    margin: 2px;\n"
"    border-radius: 6px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background: #7c9bf1;   /* Light blue highlight */\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    background: #e4ebf8;   /* Aqua click */\n"
"    color: #000000;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #e4ebf8;   /* Matches widget panels */\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #7986ac;\n"
"    padding: 6px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 6px 18px;\n"
"    background-color: transparent;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #c6d4f5;  /* Soft selec"
                        "tion */\n"
"    color: #000000;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background: #a3b1d3;\n"
"    margin: 4px 10px;\n"
"}\n"
"")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionsave)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUpscale_Image)
        self.menuEdit.addAction(self.action_move_to_input)
        self.menuView.addAction(self.actionReview)
        self.menuView.addAction(self.actionFullscreen_View)
        self.menuHelp.addAction(self.actionUpdate)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Upscaler by ICA ", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
#if QT_CONFIG(shortcut)
        self.actionsave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.action_move_to_input.setText(QCoreApplication.translate("MainWindow", u"Move to input", None))
#if QT_CONFIG(shortcut)
        self.action_move_to_input.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionFullscreen_View.setText(QCoreApplication.translate("MainWindow", u"FullScreen View", None))
#if QT_CONFIG(shortcut)
        self.actionFullscreen_View.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.actionReview.setText(QCoreApplication.translate("MainWindow", u"Review", None))
#if QT_CONFIG(shortcut)
        self.actionReview.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionUpscale_Image.setText(QCoreApplication.translate("MainWindow", u"Upscale Image", None))
#if QT_CONFIG(shortcut)
        self.actionUpscale_Image.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+U", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_pic_location.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">selected Image location</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_pic_location.setText("")
        self.lineEdit_pic_location.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Location...", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Select Image", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Preview:", None))
#if QT_CONFIG(tooltip)
        self.toolButton_browse_image.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">Shortcut = CTRL+O</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_browse_image.setText(QCoreApplication.translate("MainWindow", u"Open Image", None))
#if QT_CONFIG(tooltip)
        self.horizontalSlider_image_factor.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">Upcaling Resolution Value</span></p><p><span style=\" font-size:10pt; color:#000000;\">Shortcut for Decrease = CTRL+&lt;</span></p><p><span style=\" font-size:10pt; color:#000000;\">Shortcut for Increase = CTRL+&gt;</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Upscaling Factor", None))
#if QT_CONFIG(tooltip)
        self.toolButton_image_review.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">Shortcut = CTRL+R</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_image_review.setText(QCoreApplication.translate("MainWindow", u"Review", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"2x            3x             4x", None))
#if QT_CONFIG(tooltip)
        self.label_image_preview.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">Input Image Resolution</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_image_preview.setText(QCoreApplication.translate("MainWindow", u"Size : 360 x 360", None))
#if QT_CONFIG(tooltip)
        self.pushButton_upscale_image.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">Shortcut = CTRL+U</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_upscale_image.setText(QCoreApplication.translate("MainWindow", u"Upscale Image", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Input Image", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"OutPut Preview:", None))
#if QT_CONFIG(tooltip)
        self.toolButton_image_preview_open.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">Shortcut = CTRL+F</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_image_preview_open.setText(QCoreApplication.translate("MainWindow", u"FullScreen View", None))
#if QT_CONFIG(tooltip)
        self.pushButton_save_as_image.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">Shortcut = CTRL+S</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_save_as_image.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.textEdit_image_metadata.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Content description & metadata...(Optional)", None))
#if QT_CONFIG(tooltip)
        self.pushButton_Send_to_input.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">Shortcut = CTRL+M</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_Send_to_input.setText(QCoreApplication.translate("MainWindow", u"\u2190 Send To Input", None))
#if QT_CONFIG(tooltip)
        self.label_image_output_preview.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">Output Image Resolution</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_image_output_preview.setText(QCoreApplication.translate("MainWindow", u"Size : 1440 x 1440", None))
#if QT_CONFIG(tooltip)
        self.pushButton_save_image.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Save with metadata</p><p>Save Folder Location: Output_image</p><p><span style=\" font-size:10pt; color:#000000;\">Shortcut = CTRL+S</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_save_image.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(tooltip)
        self.toolButton_open_and_read_image.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">Shortcut = CTRL+F</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_open_and_read_image.setText(QCoreApplication.translate("MainWindow", u"Open and Read Image", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Upscaled Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Image Upscale", None))
        self.lineEdit_video_location.setText("")
        self.lineEdit_video_location.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Location...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Select Video Clip", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Preview:", None))
        self.toolButton_browse_video.setText(QCoreApplication.translate("MainWindow", u"Open Video", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Upscaling", None))
        self.toolButton_video_review.setText(QCoreApplication.translate("MainWindow", u"Review", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"2x            3x             4x", None))
        self.pushButton_extract_frames.setText(QCoreApplication.translate("MainWindow", u"Extract Frames", None))
        self.pushButton_upscale_frames.setText(QCoreApplication.translate("MainWindow", u"Upscale Frames", None))
        self.pushButton_Abort.setText(QCoreApplication.translate("MainWindow", u"Abort", None))
        self.checkBox.setText("")
        self.checkBox_2.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Factor", None))
        self.pushlButton_video_play.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Input Image", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"OutPut Preview:", None))
        self.toolButton_video_output_view.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.textEdit_video_metadata.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Content description & metadata...(Optional)", None))
        self.pushButton_save_video_with_metadata.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.toolButton_open_and_read_video.setText(QCoreApplication.translate("MainWindow", u"Open and Read Video", None))
        self.pushlButton_video_play_2.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Upscaled Clip", None))
        self.pushButton_start_upscaling_video.setText(QCoreApplication.translate("MainWindow", u"Start UpScaling", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Video Upscale", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Image Log", None))
#if QT_CONFIG(tooltip)
        self.toolButton_show_output_folder.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">Shortcut = CTRL+F</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_show_output_folder.setText(QCoreApplication.translate("MainWindow", u"Output Folder", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

