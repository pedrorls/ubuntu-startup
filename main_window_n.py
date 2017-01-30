#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
import sys
import os


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("Ubuntu Statup")
        self.home()

    def home(self):
        checkBox = QtGui.QCheckBox("InkScape", self)
        checkBox.move(50, 50)
        checkBox.stateChanged.connect(self.include_program)
        self.show()

    def include_program(self, state):
        if state == QtCore.Qt.Checked:
            os.system(
                """sudo add-apt-repository ppa:inkscape.dev/stable -y &&
                sudo apt-get update && sudo apt-get install inkscape -y"""
                )
        else:
            pass


def run():
    app = QtGui.QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
