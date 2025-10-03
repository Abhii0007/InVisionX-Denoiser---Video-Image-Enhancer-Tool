# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_viewerkhwUFc.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(945, 580)
        Form.setMinimumSize(QSize(945, 580))
        self.widget_image_output = QWidget(Form)
        self.widget_image_output.setObjectName(u"widget_image_output")
        self.widget_image_output.setGeometry(QRect(20, 60, 911, 491))
        self.widget_image_output.setMinimumSize(QSize(481, 280))
        self.widget_image_output.setStyleSheet(u"background-color: rgb(59, 65, 106);\n"
"    border: 2px solid #a5bbe6;\n"
"    border-radius: 8px;")
        self.pushButton_Save_image = QPushButton(Form)
        self.pushButton_Save_image.setObjectName(u"pushButton_Save_image")
        self.pushButton_Save_image.setGeometry(QRect(640, 20, 131, 31))
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_Save_image.setFont(font)
        self.pushButton_Save_image.setStyleSheet(u"#pushButton_Save_image{\n"
"    color: #ffffff;\n"
"    background-color: #7779eb;\n"
"    \n"
"	font: 16pt \"Cambria\";\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"#pushButton_Save_image:hover {\n"
"    background-color: #5478c7;\n"
"}\n"
"\n"
"#pushButton_Save_image:pressed {\n"
"    background-color: #204070;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"color: rgb(255,255,255);\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_Save_image:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.pushButton_add_text = QPushButton(Form)
        self.pushButton_add_text.setObjectName(u"pushButton_add_text")
        self.pushButton_add_text.setGeometry(QRect(510, 20, 121, 31))
        self.pushButton_add_text.setFont(font)
        self.pushButton_add_text.setStyleSheet(u"#pushButton_add_text{\n"
"    color: #ffffff;\n"
"    background-color: #488dfa;\n"
"    \n"
"	font: 16pt \"Cambria\";\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"#pushButton_add_text:hover {\n"
"    background-color: #5478c7;\n"
"}\n"
"\n"
"#pushButton_add_text:pressed {\n"
"    background-color: #204070;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"color: rgb(255,255,255);\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_add_text:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.pushButton_open_image = QPushButton(Form)
        self.pushButton_open_image.setObjectName(u"pushButton_open_image")
        self.pushButton_open_image.setGeometry(QRect(20, 20, 141, 31))
        font1 = QFont()
        font1.setFamilies([u"Cambria"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.pushButton_open_image.setFont(font1)
        self.pushButton_open_image.setStyleSheet(u"#pushButton_open_image{\n"
"    color: #ffffff;\n"
"    background-color: #488dfa;\n"
"    \n"
"	font: 14pt \"Cambria\";\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"#pushButton_open_image:hover {\n"
"    background-color: #5478c7;\n"
"}\n"
"\n"
"#pushButton_open_image:pressed {\n"
"    background-color: #204070;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"color: rgb(255,255,255);\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_open_image:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.pushButton_pen_tool = QPushButton(Form)
        self.pushButton_pen_tool.setObjectName(u"pushButton_pen_tool")
        self.pushButton_pen_tool.setGeometry(QRect(250, 20, 251, 31))
        self.pushButton_pen_tool.setFont(font)
        self.pushButton_pen_tool.setStyleSheet(u"#pushButton_pen_tool{\n"
"    color: #ffffff;\n"
"    background-color: #488dfa;\n"
"    \n"
"	font: 16pt \"Cambria\";\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"#pushButton_pen_tool:hover {\n"
"    background-color: #5478c7;\n"
"}\n"
"\n"
"#pushButton_pen_tool:pressed {\n"
"    background-color: #204070;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"color: rgb(255,255,255);\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_pen_tool:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.pushButton_undo = QPushButton(Form)
        self.pushButton_undo.setObjectName(u"pushButton_undo")
        self.pushButton_undo.setGeometry(QRect(170, 20, 71, 31))
        self.pushButton_undo.setFont(font1)
        self.pushButton_undo.setStyleSheet(u"#pushButton_undo{\n"
"    color: #ffffff;\n"
"    background-color: #488dfa;\n"
"    \n"
"	font: 14pt \"Cambria\";\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"#pushButton_undo:hover {\n"
"    background-color: #5478c7;\n"
"}\n"
"\n"
"#pushButton_undo:pressed {\n"
"    background-color: #204070;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"color: rgb(255,255,255);\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_undo:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Image_Viewer", None))
#if QT_CONFIG(tooltip)
        self.pushButton_Save_image.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">Shortcut = CTRL+M</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_Save_image.setText(QCoreApplication.translate("Form", u"Save Image", None))
#if QT_CONFIG(tooltip)
        self.pushButton_add_text.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">Shortcut = CTRL+M</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_add_text.setText(QCoreApplication.translate("Form", u"Add Text", None))
#if QT_CONFIG(tooltip)
        self.pushButton_open_image.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">Shortcut = CTRL+M</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_open_image.setText(QCoreApplication.translate("Form", u"Open Image", None))
#if QT_CONFIG(tooltip)
        self.pushButton_pen_tool.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">Shortcut = CTRL+M</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_pen_tool.setText(QCoreApplication.translate("Form", u"Pen  (Enable/Disable)", None))
#if QT_CONFIG(tooltip)
        self.pushButton_undo.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">Shortcut = CTRL+M</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_undo.setText(QCoreApplication.translate("Form", u"Undo", None))
    # retranslateUi

