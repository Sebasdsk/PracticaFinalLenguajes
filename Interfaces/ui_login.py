# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginuJTxFZ.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(612, 491)
        self.btnLogin = QPushButton(Login)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(260, 330, 111, 51))
        self.btnRegistro = QPushButton(Login)
        self.btnRegistro.setObjectName(u"btnRegistro")
        self.btnRegistro.setGeometry(QRect(260, 400, 111, 51))
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 70, 71, 41))
        self.label.setStyleSheet(u"font: 16pt \"Malgun Gothic\";")
        self.label_2 = QLabel(Login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 170, 121, 41))
        self.label_2.setStyleSheet(u"font: 16pt \"Malgun Gothic\";")
        self.textEdit = QTextEdit(Login)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(220, 120, 181, 31))
        self.textEdit.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.textEdit_2 = QTextEdit(Login)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(220, 210, 181, 31))
        self.textEdit_2.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.btnLogin.setText(QCoreApplication.translate("Login", u"Ingresar", None))
        self.btnRegistro.setText(QCoreApplication.translate("Login", u"Registrarse", None))
        self.label.setText(QCoreApplication.translate("Login", u"Usuario", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"Contrase\u00f1a", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("Login", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
    # retranslateUi

