from PyQt4 import QtGui, QtCore
import sys
import os


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("Ubuntu Statup")
        self.show()


def run():
    app = QtGui.QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
