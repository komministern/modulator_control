# -*- coding: utf-8 -*-

#    Copyright © 2020 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of Modulator Controller.

#import logging
from PySide2 import QtCore, QtWidgets, QtNetwork

#logger = logging.getLogger(__name__)

class MyModel(QtCore.QObject):

    command_ack = QtCore.Signal(bool)

    def __init__(self):
        super(MyModel, self).__init__()

        self.tcc_address = QtNetwork.QHostAddress('192.168.1.170')
        self.tcc_command_port = 17000

        self.local_command_port = 17000
        self.local_ack_port = 17001
        self.local_data_port = 17002

        self.charge_trig_length = 0
        self.dq_trig_delay = 0
        self.dq_trig_length = 0
        self.mod_trig_delay = 0
        self.mod_trig_length = 0
        self.mod_state = 'off'  # or 'charge' or 'modulate
        self.dq_state = 'remote'   # or 'local'

        self.sent_command_message = ''

        self.ack_timer = QtCore.QTimer()
        self.ack_timer.timeout.connect(self.message_timeout)
    
        self.init_command_socket()
        self.init_ack_socket()
        self.init_data_socket()


    def init_ack_socket(self):
        self.ack_socket = QtNetwork.QUdpSocket(self)
        self.ack_socket.bind(self.local_ack_port)
        self.ack_socket.readyRead.connect(self.read_pending_ack_datagrams)

    def init_data_socket(self):
        self.data_socket = QtNetwork.QUdpSocket(self)
        self.data_socket.bind(self.local_data_port)
        self.data_socket.readyRead.connect(self.read_pending_data_datagrams)

    def init_command_socket(self):
        self.command_socket = QtNetwork.QUdpSocket(self)
        self.command_socket.bind(self.local_command_port)
        self.command_socket.readyRead.connect(self.read_pending_command_datagrams)


    def quit(self):
        self.ack_socket.close()
        QtWidgets.QApplication.quit()

    def set_mod_state(self, state):
        self.mod_state = state

    def set_dq_state(self, state):
        self.dq_state = state

    def send_command(self):
        sequence = (str(self.charge_trig_length), str(self.dq_trig_delay), str(self.dq_trig_length), str(self.mod_trig_delay), str(self.mod_trig_length), str(self.mod_state), str(self.dq_state))
        
        message = ','.join(sequence)

        self.sent_command_message = message
        self.ack_timer.start(100)

        self.ack_socket.writeDatagram(message.encode('utf-8'), self.tcc_address, self.tcc_command_port)

    def message_timeout(self):
        self.ack_timer.stop()
        self.command_ack.emit(False)
        print('Ack timeout.')



    def read_pending_ack_datagrams(self):

        while self.ack_socket.hasPendingDatagrams():
            
            datagram = QtCore.QByteArray()
            datagram.resize(self.ack_socket.pendingDatagramSize())

            datagram, sender_address, sender_port = self.ack_socket.readDatagram(datagram.size())

            ack_message = datagram.data().decode('utf-8')

            if ack_message == self.sent_command_message:
                self.ack_timer.stop()
                self.command_ack.emit(True)

                print('Received ack: ' + ack_message)

            else:

                print('Received erroneous ack: ' + ack_message)
                self.command_ack.emit(False)


    def read_pending_data_datagrams(self):

        while self.data_socket.hasPendingDatagrams():

            datagram = QtCore.QByteArray()
            datagram.resize(self.data_socket.pendingDatagramSize())

            datagram, sender_address, sender_port = self.data_socket.readDatagram(datagram.size())

            data_message = datagram.data().decode('utf-8')

            print('Received data: ' + data_message)

            #DOSTUFF
                

    def read_pending_command_datagrams(self):

        while self.command_socket.hasPendingDatagrams():

            datagram = QtCore.QByteArray()
            datagram.resize(self.command_socket.pendingDatagramSize())

            datagram, sender_address, sender_port = self.command_socket.readDatagram(datagram.size())

            command_message = datagram.data().decode('utf-8')

            print('Received command: ' + command_message)

            #DOSTUFF
                


