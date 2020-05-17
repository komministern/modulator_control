# -*- coding: utf-8 -*-
#
#    Copyright © 2020 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of the FMTS modulator control.

import sys
import logging
from PySide2 import QtWidgets
from view.view import MyView
from presenter.presenter import MyPresenter
from model.model import MyModel

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    model = MyModel()
    view = MyView() 
    presenter = MyPresenter(model, view, app)
    view.show()

    sys.exit(app.exec_())
