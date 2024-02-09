# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'myui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1056, 723)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(480, 20, 651, 661))
        self.stackedWidget.setLineWidth(0)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.label = QLabel(self.home)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 260, 301, 111))
        self.stackedWidget.addWidget(self.home)
        self.test = QWidget()
        self.test.setObjectName(u"test")
        self.pushButton = QPushButton(self.test)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 120, 339, 91))
        self.pushButton_2 = QPushButton(self.test)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(200, 270, 339, 91))
        self.pushButton_3 = QPushButton(self.test)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(200, 430, 339, 91))
        self.stackedWidget.addWidget(self.test)
        self.predict = QWidget()
        self.predict.setObjectName(u"predict")
        self.pushButton_5 = QPushButton(self.predict)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(190, 410, 371, 111))
        self.pushButton_4 = QPushButton(self.predict)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(190, 200, 371, 111))
        self.stackedWidget.addWidget(self.predict)
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(70, 60, 301, 171))
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(70, 270, 301, 181))
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(70, 480, 301, 181))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1056, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.stackedWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u6b22\u8fce\u8fdb\u5165\u667a\u80fd\u4ea4\u901a\u8def\u6807\u8bc6\u522b\u7cfb\u7edf</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84\u6d4b\u8bd5", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u8bfb\u53d6\u6d4b\u8bd5", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u9884\u6d4b\u6d4b\u8bd5", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Camera Stream Detect (\u6d41\u68c0\u6d4b)", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Camera SnapShot Detect (\u5e27\u68c0\u6d4b)", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Test Submodule", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Detect Submodule", None))
    # retranslateUi

