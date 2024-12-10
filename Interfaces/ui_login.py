# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginOtshCo.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

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
        self.txtPass = QLineEdit(Login)
        self.txtPass.setObjectName(u"txtPass")
        self.txtPass.setGeometry(QRect(220, 210, 181, 31))
        self.txtPass.setEchoMode(QLineEdit.EchoMode.Password)
        self.txtUsuario = QLineEdit(Login)
        self.txtUsuario.setObjectName(u"txtUsuario")
        self.txtUsuario.setGeometry(QRect(220, 120, 181, 31))

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.btnLogin.setText(QCoreApplication.translate("Login", u"Ingresar", None))
        self.btnRegistro.setText(QCoreApplication.translate("Login", u"Registrarse", None))
        self.label.setText(QCoreApplication.translate("Login", u"Usuario", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"Contrase\u00f1a", None))
        self.txtPass.setText("")
        self.txtUsuario.setText("")
    # retranslateUi

