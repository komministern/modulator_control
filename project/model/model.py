#!python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.

#import logging
from PySide2 import QtCore, QtWidgets, QtNetwork

#logger = logging.getLogger(__name__)

class MyModel(QtCore.QObject):

    command_response = QtCore.Signal(bool)

    def __init__(self):
        super(MyModel, self).__init__()

        self.tcc_address = QtNetwork.QHostAddress('192.168.1.170')
        self.tcc_port = 17000

        self.charge_trig_length = 0
        self.dq_trig_delay = 0
        self.mod_trig_delay = 0
        self.mod_trig_length = 0
        self.mod_state = 'off'  # or 'charge' or 'modulate
        self.dq_state = 'off'   # or 'on' or remote

        self.sent_message = ''

        self.response_timer = QtCore.QTimer()
        self.response_timer.timeout.connect(self.message_timeout)
    
        self.init_socket()


    def init_socket(self):
        self.udp_socket = QtNetwork.QUdpSocket(self)
        #self.udp_socket.bind(QtNetwork.QHostAddress('127.0.0.1'), 16999)
        self.udp_socket.bind(16999)
        self.udp_socket.readyRead.connect(self.read_pending_datagrams)

    def quit(self):
        self.udp_socket.close()
        QtWidgets.QApplication.quit()

    def set_mod_state(self, state):
        self.mod_state = state

    def set_dq_state(self, state):
        self.dq_state = state

    def send_settings(self):
        #print('Sending....')
        sequence = (str(self.charge_trig_length), str(self.dq_trig_delay), str(self.mod_trig_delay), str(self.mod_trig_length), str(self.mod_state), str(self.dq_state))
        message = ','.join(sequence)

        self.sent_message = message
        self.response_timer.start(1000)

        self.udp_socket.writeDatagram(message.encode('utf-8'), self.tcc_address, self.tcc_port)

    def message_timeout(self):
        self.response_timer.stop()
        self.command_response.emit(False)
        


    def read_pending_datagrams(self):
        while self.udp_socket.hasPendingDatagrams():
            
            datagram = QtCore.QByteArray()
            datagram.resize(self.udp_socket.pendingDatagramSize())

            datagram, sender_address, sender_port = self.udp_socket.readDatagram(datagram.size())

            received_message = datagram.data().decode('utf-8')

            if received_message == self.sent_message:
                self.response_timer.stop()
                self.command_response.emit(True)

                print(received_message)

            else:
                print('Received different answer. (' + received_message + ')')

                


