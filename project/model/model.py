#!python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.

#import logging
from PySide2 import QtCore, QtWidgets, QtNetwork

#logger = logging.getLogger(__name__)

class MyModel(QtCore.QObject):

    def __init__(self):
        super(MyModel, self).__init__()

        self.charge_trig_length = 0
        self.dq_trig_delay = 0
        self.mod_trig_delay = 0
        self.mod_trig_length = 0

        self.init_socket()


    def init_socket(self):
        self.udp_socket = QtNetwork.QUdpSocket(self)
        #self.udp_socket.bind(QtNetwork.QHostAddress('127.0.0.1'), 16999)
        self.udp_socket.bind(16999)
        self.udp_socket.readyRead.connect(self.read_pending_datagrams)

    def quit(self):
        QtWidgets.QApplication.quit()

    def send_settings(self):
        print('Sending....')
        self.udp_socket.writeDatagram(bytes('Jesus Lever!', 'utf-8'), QtNetwork.QHostAddress('192.168.1.170'), 17000)

    def read_pending_datagrams(self):
        while self.udp_socket.hasPendingDatagrams():
            datagram = QtCore.QByteArray()
            datagram.resize(self.udp_socket.pendingDatagramSize())

            datagram, sender_address, sender_port = self.udp_socket.readDatagram(datagram.size())

            print('Received...')

            print(type(datagram))
            print(datagram)

