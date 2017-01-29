#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from subprocess import Popen, PIPE
import sys
import time


class PassWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(PassWindow, self).__init__(parent)
        self.setWindowTitle("Root Password")
        self.home()

    def home(self):
        self.label = QtGui.QLabel("Please, type your password")
        self.lineedit = QtGui.QLineEdit("KwSagitarii+11")
        self.lineedit.setFocus()
        self.lineedit.setEchoMode(QtGui.QLineEdit.Password)

        self.btnOk = QtGui.QPushButton("OK")
        self.btnOk.clicked.connect(self.show_result)

        self.btnCancel = QtGui.QPushButton("Cancel")
        self.btnCancel.clicked.connect(self.exit)

        layoutH = QtGui.QHBoxLayout()
        layoutH.addWidget(self.btnOk)
        layoutH.addWidget(self.btnCancel)

        layoutV = QtGui.QVBoxLayout()
        layoutV.addWidget(self.label)
        layoutV.addWidget(self.lineedit)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

        self.show()

    def show_result(self):
        pass

    def exit(self):
        sys.exit()


def run():
    app = QtGui.QApplication(sys.argv)
    win = PassWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
