# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 431)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_7 = QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_2 = QGroupBox(self.groupBox_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_modTrigDelay = QLineEdit(self.groupBox_2)
        self.lineEdit_modTrigDelay.setObjectName(u"lineEdit_modTrigDelay")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_modTrigDelay.sizePolicy().hasHeightForWidth())
        self.lineEdit_modTrigDelay.setSizePolicy(sizePolicy)
        self.lineEdit_modTrigDelay.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_modTrigDelay, 0, 1, 1, 1)

        self.horizontalSlider_modTrigDelay = QSlider(self.groupBox_2)
        self.horizontalSlider_modTrigDelay.setObjectName(u"horizontalSlider_modTrigDelay")
        self.horizontalSlider_modTrigDelay.setMinimum(400)
        self.horizontalSlider_modTrigDelay.setMaximum(600)
        self.horizontalSlider_modTrigDelay.setSingleStep(1)
        self.horizontalSlider_modTrigDelay.setValue(400)
        self.horizontalSlider_modTrigDelay.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider_modTrigDelay, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.groupBox = QGroupBox(self.groupBox_6)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_chargeTrigLength = QLineEdit(self.groupBox)
        self.lineEdit_chargeTrigLength.setObjectName(u"lineEdit_chargeTrigLength")
        sizePolicy.setHeightForWidth(self.lineEdit_chargeTrigLength.sizePolicy().hasHeightForWidth())
        self.lineEdit_chargeTrigLength.setSizePolicy(sizePolicy)
        self.lineEdit_chargeTrigLength.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_chargeTrigLength, 0, 1, 1, 1)

        self.horizontalSlider_chargeTrigLength = QSlider(self.groupBox)
        self.horizontalSlider_chargeTrigLength.setObjectName(u"horizontalSlider_chargeTrigLength")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalSlider_chargeTrigLength.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_chargeTrigLength.setSizePolicy(sizePolicy1)
        self.horizontalSlider_chargeTrigLength.setMinimum(300)
        self.horizontalSlider_chargeTrigLength.setMaximum(400)
        self.horizontalSlider_chargeTrigLength.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider_chargeTrigLength, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.groupBox_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_6 = QGridLayout(self.groupBox_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_dqTrigDelay = QLineEdit(self.groupBox_7)
        self.lineEdit_dqTrigDelay.setObjectName(u"lineEdit_dqTrigDelay")
        sizePolicy.setHeightForWidth(self.lineEdit_dqTrigDelay.sizePolicy().hasHeightForWidth())
        self.lineEdit_dqTrigDelay.setSizePolicy(sizePolicy)
        self.lineEdit_dqTrigDelay.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_dqTrigDelay, 0, 1, 1, 1)

        self.horizontalSlider_dqTrigDelay = QSlider(self.groupBox_7)
        self.horizontalSlider_dqTrigDelay.setObjectName(u"horizontalSlider_dqTrigDelay")
        sizePolicy1.setHeightForWidth(self.horizontalSlider_dqTrigDelay.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_dqTrigDelay.setSizePolicy(sizePolicy1)
        self.horizontalSlider_dqTrigDelay.setMinimum(240)
        self.horizontalSlider_dqTrigDelay.setMaximum(280)
        self.horizontalSlider_dqTrigDelay.setValue(240)
        self.horizontalSlider_dqTrigDelay.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.horizontalSlider_dqTrigDelay, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_7, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox_6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_modTrigLength = QLineEdit(self.groupBox_3)
        self.lineEdit_modTrigLength.setObjectName(u"lineEdit_modTrigLength")
        sizePolicy.setHeightForWidth(self.lineEdit_modTrigLength.sizePolicy().hasHeightForWidth())
        self.lineEdit_modTrigLength.setSizePolicy(sizePolicy)
        self.lineEdit_modTrigLength.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_modTrigLength, 0, 1, 1, 1)

        self.horizontalSlider_modTrigLength = QSlider(self.groupBox_3)
        self.horizontalSlider_modTrigLength.setObjectName(u"horizontalSlider_modTrigLength")
        self.horizontalSlider_modTrigLength.setMinimum(25)
        self.horizontalSlider_modTrigLength.setMaximum(200)
        self.horizontalSlider_modTrigLength.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.horizontalSlider_modTrigLength, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_3, 3, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_6, 0, 0, 1, 2)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.radioButton_Off = QRadioButton(self.groupBox_4)
        self.radioButton_Off.setObjectName(u"radioButton_Off")

        self.gridLayout_4.addWidget(self.radioButton_Off, 0, 0, 1, 1)

        self.radioButton_Charge = QRadioButton(self.groupBox_4)
        self.radioButton_Charge.setObjectName(u"radioButton_Charge")

        self.gridLayout_4.addWidget(self.radioButton_Charge, 0, 1, 1, 1)

        self.radioButton_Modulate = QRadioButton(self.groupBox_4)
        self.radioButton_Modulate.setObjectName(u"radioButton_Modulate")

        self.gridLayout_4.addWidget(self.radioButton_Modulate, 0, 2, 1, 1)

        self.pushButton_Apply = QPushButton(self.groupBox_4)
        self.pushButton_Apply.setObjectName(u"pushButton_Apply")

        self.gridLayout_4.addWidget(self.pushButton_Apply, 0, 3, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_4, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 780, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Modulator Control", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Triggers", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Mod Trig Delay", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Charge Trig Length", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"DQ Trig Delay", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Mod Trig Length", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Control", None))
        self.radioButton_Off.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.radioButton_Charge.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.radioButton_Modulate.setText(QCoreApplication.translate("MainWindow", u"Modulate", None))
        self.pushButton_Apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
    # retranslateUi

