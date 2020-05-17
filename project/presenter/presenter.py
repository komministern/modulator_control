# -*- coding: utf-8 -*-
#
#    Copyright © 2020 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of the FMTS modulator control.

from PySide2 import QtCore

class MyPresenter(QtCore.QObject):

    def __init__(self, model, view, app):
        super(MyPresenter, self).__init__()

        # Store view and model.
        self.model = model
        self.view = view
        self.app = app

        self.view.horizontalSlider_chargeTrigLength.setValue(350)
        self.set_charge_trig_length(350)

        self.view.horizontalSlider_dqTrigDelay.setValue(250)
        self.set_dq_trig_delay(250)

        self.view.horizontalSlider_dqTrigLength.setValue(2)
        self.set_dq_trig_length(2)

        self.view.horizontalSlider_modTrigDelay.setValue(400)
        self.set_mod_trig_delay(400)

        self.view.horizontalSlider_modTrigLength.setValue(30)
        self.set_mod_trig_length(30)

        self.set_sync_state(False)

        self.connect_signals()

        

    def connect_signals(self):
        self.view.quit.connect(self.model.quit)

        self.model.command_ack.connect(self.set_sync_state)
        self.model.log.connect(self.log)

        self.view.pushButton_Apply.pressed.connect(self.apply_settings)

        self.view.radioButton_Modulate.pressed.connect(self.set_modulate_state)
        self.view.radioButton_Charge.pressed.connect(self.set_charge_state)
        self.view.radioButton_Off.pressed.connect(self.set_off_state)

        self.view.radioButton_DQ_Local.pressed.connect(self.set_dq_local)
        self.view.radioButton_DQ_Remote.pressed.connect(self.set_dq_remote)

        self.view.horizontalSlider_chargeTrigLength.valueChanged.connect(self.set_charge_trig_length)
        self.view.horizontalSlider_dqTrigDelay.valueChanged.connect(self.set_dq_trig_delay)
        self.view.horizontalSlider_dqTrigLength.valueChanged.connect(self.set_dq_trig_length)
        self.view.horizontalSlider_modTrigDelay.valueChanged.connect(self.set_mod_trig_delay)
        self.view.horizontalSlider_modTrigLength.valueChanged.connect(self.set_mod_trig_length)

    def set_off_state(self):
        self.model.set_mod_state('off')
        self.set_sync_state(False)
    
    def set_charge_state(self):
        self.model.set_mod_state('charge')
        self.set_sync_state(False)

    def set_modulate_state(self):
        self.model.set_mod_state('modulate')
        self.set_sync_state(False)
    
    def set_dq_remote(self):
        self.model.set_dq_state('remote')
        self.view.horizontalSlider_dqTrigDelay.setEnabled(True)
        self.set_sync_state(False)

    def set_dq_local(self):
        self.model.set_dq_state('local')
        self.view.horizontalSlider_dqTrigDelay.setEnabled(False)
        self.set_sync_state(False)


    def set_sync_state(self, status):
        if status == True:
            self.view.label_Sync.setStyleSheet("QLabel { background-color : green; }")
        else:
            self.view.label_Sync.setStyleSheet("QLabel { background-color : yellow; }")

    def set_charge_trig_length(self, value):
        self.model.charge_trig_length = value
        self.view.lineEdit_chargeTrigLength.setText(str(value) + ' μs')
        self.set_sync_state(False)

    def set_dq_trig_delay(self, value):
        self.model.dq_trig_delay = value
        self.view.lineEdit_dqTrigDelay.setText(str(value) + ' μs')
        self.set_sync_state(False)

    def set_dq_trig_length(self, value):
        self.model.dq_trig_length = value
        self.view.lineEdit_dqTrigLength.setText(str(value) + ' μs')
        self.set_sync_state(False)

    def set_mod_trig_delay(self, value):
        self.model.mod_trig_delay = value
        self.view.lineEdit_modTrigDelay.setText(str(value) + ' μs')
        self.set_sync_state(False)

    def set_mod_trig_length(self, value):
        self.model.mod_trig_length = value
        self.view.lineEdit_modTrigLength.setText(str(value) + ' μs')
        self.set_sync_state(False)

    def apply_settings(self):

        # CHECKS

        if self.model.charge_trig_length >= self.model.mod_trig_delay:
            self.log('INFO: Mod Trig Delay must be greater than Charge Trig Length.')
        elif self.model.dq_trig_delay > self.model.charge_trig_length:
            self.log('INFO: DQ Trig Delay must be less than Charge Trig Length.')
        else:
            self.model.send_command()

    
    def log(self, text):
        from datetime import datetime
        time = datetime.now().strftime('%H:%M:%S - ')
        self.view.textEdit_Status.append(time + text)

