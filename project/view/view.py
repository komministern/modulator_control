# -*- coding: utf-8 -*-
#
#    Copyright © 2020 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of the FMTS modulator control.

from PySide2 import QtCore, QtWidgets, QtGui
from view.ui_mainwindow import Ui_MainWindow

class MyView(QtWidgets.QMainWindow, Ui_MainWindow):

    quit = QtCore.Signal()

    def __init__(self):
        super(MyView, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('radar.png'))
        

    def closeEvent(self, event):
        event.ignore()
        self.quit.emit() 
