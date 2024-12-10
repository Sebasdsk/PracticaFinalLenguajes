# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'estadisticaVAbCLc.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_FormEstats(object):
    def setupUi(self, FormEstats):
        if not FormEstats.objectName():
            FormEstats.setObjectName(u"FormEstats")
        FormEstats.resize(597, 479)
        font = QFont()
        font.setBold(False)
        FormEstats.setFont(font)
        self.tableWidget = QTableWidget(FormEstats)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(90, 140, 421, 192))
        self.btnSalir = QPushButton(FormEstats)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(90, 410, 101, 51))
        self.btnExportar = QPushButton(FormEstats)
        self.btnExportar.setObjectName(u"btnExportar")
        self.btnExportar.setGeometry(QRect(360, 410, 111, 51))

        self.retranslateUi(FormEstats)

        QMetaObject.connectSlotsByName(FormEstats)
    # setupUi

    def retranslateUi(self, FormEstats):
        FormEstats.setWindowTitle(QCoreApplication.translate("FormEstats", u"Estadistica", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormEstats", u"Usuario", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormEstats", u"Partidas Jugadas", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormEstats", u"Partidas Ganadas", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormEstats", u"Partidas Perdidas", None));
        self.btnSalir.setText(QCoreApplication.translate("FormEstats", u"Salir", None))
        self.btnExportar.setText(QCoreApplication.translate("FormEstats", u"Exportar a PDF", None))
    # retranslateUi

