#!python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.

from PySide2 import QtCore

class MyPresenter(QtCore.QObject):

    def __init__(self, model, view, app):
        super(MyPresenter, self).__init__()

        # Store view and model.
        self.model = model
        self.view = view
        self.app = app

        self.view.horizontalSlider_chargeTrigLength.setValue(300)
        self.new_charge_trig_length(300)

        self.view.horizontalSlider_dqTrigDelay.setValue(240)
        self.new_dq_trig_delay(240)

        self.view.horizontalSlider_modTrigDelay.setValue(400)
        self.new_mod_trig_delay(400)

        self.view.horizontalSlider_modTrigLength.setValue(30)
        self.new_mod_trig_length(30)

        self.view.pushButton_off.setEnabled(False)

        self.connect_signals()

        

    def connect_signals(self):
        self.view.quit.connect(self.model.quit)
        #self.view.pushButton.pressed.connect(self.model.quit)

        self.view.horizontalSlider_chargeTrigLength.valueChanged.connect(self.new_charge_trig_length)
        self.view.horizontalSlider_dqTrigDelay.valueChanged.connect(self.new_dq_trig_delay)
        self.view.horizontalSlider_modTrigDelay.valueChanged.connect(self.new_mod_trig_delay)
        self.view.horizontalSlider_modTrigLength.valueChanged.connect(self.new_mod_trig_length)


    def new_charge_trig_length(self, value):
        self.view.lineEdit_chargeTrigLength.setText(str(value) + ' μs')

    def new_dq_trig_delay(self, value):
        self.view.lineEdit_dqTrigDelay.setText(str(value) + ' μs')

    def new_mod_trig_delay(self, value):
        self.view.lineEdit_modTrigDelay.setText(str(value) + ' μs')

    def new_mod_trig_length(self, value):
        self.view.lineEdit_modTrigLength.setText(str(value) + ' μs')
