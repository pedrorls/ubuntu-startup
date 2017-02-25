from PyQt4 import QtGui
from gui_window import Ui_MainWindow
import sys


def run():
    app = QtGui.QApplication(sys.argv)
    win = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
