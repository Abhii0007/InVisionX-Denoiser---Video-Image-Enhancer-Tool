# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutyRYHLr.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QTextEdit,
    QWidget)

class Ui_about(object):
    def setupUi(self, about):
        if not about.objectName():
            about.setObjectName(u"about")
        about.resize(530, 560)
        about.setMinimumSize(QSize(530, 560))
        about.setMaximumSize(QSize(530, 560))
        self.textEdit_about = QTextEdit(about)
        self.textEdit_about.setObjectName(u"textEdit_about")
        self.textEdit_about.setGeometry(QRect(0, 0, 530, 560))
        self.textEdit_about.setStyleSheet(u"background-color: rgb(47, 59, 100);")
        self.textEdit_about.setReadOnly(True)
        self.textEdit_about.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.retranslateUi(about)

        QMetaObject.connectSlotsByName(about)
    # setupUi

    def retranslateUi(self, about):
        about.setWindowTitle(QCoreApplication.translate("about", u"About", None))
        self.textEdit_about.setHtml(QCoreApplication.translate("about", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<h1 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700; color:#45ffc1;\">About</span></h1>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#7895ff;\">    </span><span style=\" font-size:10pt; font-weight:700; color:#7895ff;\">Developer:</span><span style=\" font-size:10pt; color:#7895ff;\"> A"
                        "bhishek Verma<br />    </span><span style=\" font-size:10pt; font-weight:700; color:#7895ff;\">Project:</span><span style=\" font-size:10pt; color:#7895ff;\"> BTech Project7<br />    </span><span style=\" font-size:10pt; font-weight:700; color:#7895ff;\">Branch:</span><span style=\" font-size:10pt; color:#7895ff;\"> CS-AIML, 7th Sem April 2024<br />    </span><span style=\" font-size:10pt; font-weight:700; color:#7895ff;\">License:</span><span style=\" font-size:10pt; color:#7895ff;\"> Open Source GNU</span></p>\n"
"<h2 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; color:#45ffc1;\">Description</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:500; color:#7895ff;\">The </span><span style=\" font-size:10pt; font-weight:700; color:#7895ff;\">AI Image &amp; Video U"
                        "pscaler Tool</span><span style=\" font-size:11pt; font-weight:500; color:#7895ff;\"> is a user-friendly software powered by the     </span><span style=\" font-size:10pt; font-weight:700; color:#7895ff;\">Real-ESRGAN (Generative Adversarial Network)</span><span style=\" font-size:11pt; font-weight:500; color:#7895ff;\"> model. It enables users to regenerate, restore, and upscale images and videos with exceptional clarity and detail. With its simple and intuitive GUI, advanced AI-based super-resolution is now accessible to everyone.</span></p>\n"
"<h2 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; color:#45ffc1;\">Features</span></h2>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:10pt; color:#7895ff;\" style=\" margin-top:8px; margin-bottom:6px; margin-left:20px; margin-right:0px; -qt-block-indent:0; "
                        "text-indent:0px;\"><span style=\" font-weight:700;\">AI-Powered Upscaling:</span> Improves image and video resolution using Real-ESRGAN.<span style=\" color:#1e1e1e;\">    </span></li>\n"
"<li style=\" font-size:10pt; color:#7895ff;\" style=\" margin-top:6px; margin-bottom:6px; margin-left:20px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">User-friendly Interface:</span> Intuitive design for smooth navigation and operation.<span style=\" color:#1e1e1e;\">    </span></li>\n"
"<li style=\" font-size:10pt; color:#7895ff;\" style=\" margin-top:6px; margin-bottom:6px; margin-left:20px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Batch Processing:</span> Upscale multiple images/videos simultaneously.<span style=\" color:#1e1e1e;\">    </span></li>\n"
"<li style=\" font-size:10pt; color:#7895ff;\" style=\" margin-top:6px; margin-bottom:6px; margin-left:20px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style"
                        "=\" font-weight:700;\">Cross-format Support:</span> Compatible with popular image and video formats.<span style=\" color:#1e1e1e;\">    </span></li>\n"
"<li style=\" font-size:10pt; color:#7895ff;\" style=\" margin-top:6px; margin-bottom:8px; margin-left:20px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Efficient Processing:</span> Optimized for both CPU and GPU acceleration.</li></ul>\n"
"<h2 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; color:#45ffc1;\">License</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#7895ff;\">    This software is released under the </span><span style=\" font-size:10pt; font-weight:700; color:#7895ff;\">Open Source GNU License</span><span style=\" font-size:10pt; color:#7895ff;\">, allowing "
                        "users to freely     use, modify, and distribute it, while ensuring that derivative works remain open source.</span></p>\n"
"<h2 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; color:#45ffc1;\">Contact</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#7895ff;\">    For inquiries or support, please contact: </span><span style=\" font-size:10pt; font-weight:700; color:#7895ff;\">abhi639679@gmail.com</span></p></body></html>", None))
    # retranslateUi

