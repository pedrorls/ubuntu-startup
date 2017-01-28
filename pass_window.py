from PyQt4 import QtGui, QtCore
import sys
import os
import getpass


class PassWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(PassWindow, self).__init__(parent)
        self.setWindowTitle("Root Password")
        self.home()

    def home(self):
        self.label = QtGui.QLabel("Please, type your password")
        self.lineedit = QtGui.QLineEdit(self)
        self.lineedit.setFocus()
        self.lineedit.setEchoMode(QtGui.QLineEdit.Password)

        self.btnOk = QtGui.QPushButton("OK")
        self.btnOk.clicked.connect(self.show_result)

        self.btnCancel = QtGui.QPushButton("Cancel")
        self.btnCancel.clicked.connect(self.exit)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineedit)
        layout.addWidget(self.btnOk)
        layout.addWidget(self.btnCancel)
        self.setLayout(layout)

        self.show()

    def show_result(self):
        print(self.lineedit.text())

    def exit(self):
        sys.exit()


def run():
    app = QtGui.QApplication(sys.argv)
    win = PassWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
