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
        MainWindow.resize(837, 430)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_9 = QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.radioButton_DQ_Remote = QRadioButton(self.groupBox_5)
        self.radioButton_DQ_Remote.setObjectName(u"radioButton_DQ_Remote")
        self.radioButton_DQ_Remote.setChecked(True)

        self.gridLayout_5.addWidget(self.radioButton_DQ_Remote, 0, 1, 1, 1)

        self.radioButton_DQ_Local = QRadioButton(self.groupBox_5)
        self.radioButton_DQ_Local.setObjectName(u"radioButton_DQ_Local")
        self.radioButton_DQ_Local.setEnabled(False)

        self.gridLayout_5.addWidget(self.radioButton_DQ_Local, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_5, 2, 1, 1, 1)

        self.groupBox_8 = QGroupBox(self.centralwidget)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_8 = QGridLayout(self.groupBox_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer = QSpacerItem(115, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.pushButton_Apply = QPushButton(self.groupBox_8)
        self.pushButton_Apply.setObjectName(u"pushButton_Apply")

        self.gridLayout_8.addWidget(self.pushButton_Apply, 0, 1, 1, 1)

        self.label_Sync = QLabel(self.groupBox_8)
        self.label_Sync.setObjectName(u"label_Sync")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_Sync.sizePolicy().hasHeightForWidth())
        self.label_Sync.setSizePolicy(sizePolicy1)
        self.label_Sync.setFrameShape(QFrame.Box)
        self.label_Sync.setAlignment(Qt.AlignCenter)
        self.label_Sync.setMargin(5)

        self.gridLayout_8.addWidget(self.label_Sync, 0, 2, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_8, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.radioButton_Off = QRadioButton(self.groupBox_4)
        self.radioButton_Off.setObjectName(u"radioButton_Off")
        self.radioButton_Off.setChecked(True)

        self.gridLayout_4.addWidget(self.radioButton_Off, 0, 0, 1, 1)

        self.radioButton_Charge = QRadioButton(self.groupBox_4)
        self.radioButton_Charge.setObjectName(u"radioButton_Charge")

        self.gridLayout_4.addWidget(self.radioButton_Charge, 0, 1, 1, 1)

        self.radioButton_Modulate = QRadioButton(self.groupBox_4)
        self.radioButton_Modulate.setObjectName(u"radioButton_Modulate")

        self.gridLayout_4.addWidget(self.radioButton_Modulate, 0, 2, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_4, 2, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_7 = QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox = QGroupBox(self.groupBox_6)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSlider_chargeTrigLength = QSlider(self.groupBox)
        self.horizontalSlider_chargeTrigLength.setObjectName(u"horizontalSlider_chargeTrigLength")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.horizontalSlider_chargeTrigLength.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_chargeTrigLength.setSizePolicy(sizePolicy2)
        self.horizontalSlider_chargeTrigLength.setMinimum(300)
        self.horizontalSlider_chargeTrigLength.setMaximum(400)
        self.horizontalSlider_chargeTrigLength.setOrientation(Qt.Horizontal)
        self.horizontalSlider_chargeTrigLength.setTickPosition(QSlider.NoTicks)

        self.gridLayout.addWidget(self.horizontalSlider_chargeTrigLength, 0, 0, 1, 1)

        self.lineEdit_chargeTrigLength = QLineEdit(self.groupBox)
        self.lineEdit_chargeTrigLength.setObjectName(u"lineEdit_chargeTrigLength")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_chargeTrigLength.sizePolicy().hasHeightForWidth())
        self.lineEdit_chargeTrigLength.setSizePolicy(sizePolicy3)
        self.lineEdit_chargeTrigLength.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_chargeTrigLength.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_chargeTrigLength.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_chargeTrigLength, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.groupBox_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_6 = QGridLayout(self.groupBox_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_dqTrigDelay = QLineEdit(self.groupBox_7)
        self.lineEdit_dqTrigDelay.setObjectName(u"lineEdit_dqTrigDelay")
        sizePolicy3.setHeightForWidth(self.lineEdit_dqTrigDelay.sizePolicy().hasHeightForWidth())
        self.lineEdit_dqTrigDelay.setSizePolicy(sizePolicy3)
        self.lineEdit_dqTrigDelay.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_dqTrigDelay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_dqTrigDelay.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_dqTrigDelay, 0, 1, 1, 1)

        self.horizontalSlider_dqTrigDelay = QSlider(self.groupBox_7)
        self.horizontalSlider_dqTrigDelay.setObjectName(u"horizontalSlider_dqTrigDelay")
        sizePolicy2.setHeightForWidth(self.horizontalSlider_dqTrigDelay.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_dqTrigDelay.setSizePolicy(sizePolicy2)
        self.horizontalSlider_dqTrigDelay.setMinimum(240)
        self.horizontalSlider_dqTrigDelay.setMaximum(280)
        self.horizontalSlider_dqTrigDelay.setPageStep(5)
        self.horizontalSlider_dqTrigDelay.setValue(240)
        self.horizontalSlider_dqTrigDelay.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.horizontalSlider_dqTrigDelay, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_7, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.groupBox_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_modTrigDelay = QLineEdit(self.groupBox_2)
        self.lineEdit_modTrigDelay.setObjectName(u"lineEdit_modTrigDelay")
        sizePolicy3.setHeightForWidth(self.lineEdit_modTrigDelay.sizePolicy().hasHeightForWidth())
        self.lineEdit_modTrigDelay.setSizePolicy(sizePolicy3)
        self.lineEdit_modTrigDelay.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_modTrigDelay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
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

        self.groupBox_3 = QGroupBox(self.groupBox_6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_modTrigLength = QLineEdit(self.groupBox_3)
        self.lineEdit_modTrigLength.setObjectName(u"lineEdit_modTrigLength")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit_modTrigLength.sizePolicy().hasHeightForWidth())
        self.lineEdit_modTrigLength.setSizePolicy(sizePolicy4)
        self.lineEdit_modTrigLength.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_modTrigLength.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_modTrigLength.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_modTrigLength, 0, 1, 1, 1)

        self.horizontalSlider_modTrigLength = QSlider(self.groupBox_3)
        self.horizontalSlider_modTrigLength.setObjectName(u"horizontalSlider_modTrigLength")
        self.horizontalSlider_modTrigLength.setMinimum(25)
        self.horizontalSlider_modTrigLength.setMaximum(200)
        self.horizontalSlider_modTrigLength.setPageStep(5)
        self.horizontalSlider_modTrigLength.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.horizontalSlider_modTrigLength, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_3, 3, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_6, 0, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 837, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Modulator Control", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"DQ", None))
        self.radioButton_DQ_Remote.setText(QCoreApplication.translate("MainWindow", u"Remote", None))
        self.radioButton_DQ_Local.setText(QCoreApplication.translate("MainWindow", u"Local", None))
        self.groupBox_8.setTitle("")
        self.pushButton_Apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.label_Sync.setText(QCoreApplication.translate("MainWindow", u"Synchronized", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Modulator", None))
        self.radioButton_Off.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.radioButton_Charge.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.radioButton_Modulate.setText(QCoreApplication.translate("MainWindow", u"Modulate", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Triggers", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Charge Trig Length", None))
        self.lineEdit_chargeTrigLength.setText(QCoreApplication.translate("MainWindow", u"12345 us", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"DQ Trig Delay", None))
        self.lineEdit_dqTrigDelay.setText(QCoreApplication.translate("MainWindow", u"12345 us", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Mod Trig Delay", None))
        self.lineEdit_modTrigDelay.setText(QCoreApplication.translate("MainWindow", u"12345 us", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Mod Trig Length", None))
        self.lineEdit_modTrigLength.setText(QCoreApplication.translate("MainWindow", u"12345 us", None))
    # retranslateUi

