# -*- coding: utf-8 -*-

# Created by: Pedro Rodrigues Lima da Silva
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(550, 500))
        MainWindow.setMaximumSize(QtCore.QSize(550, 500))
        MainWindow.setWindowTitle(_fromUtf8(""))
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8(
                "QPushButton {\n"
                "border-radius: 10px;\n"
                "}\n"
                "\n"
                "QListView {\n"
                "    background-color: rgb(172,172,172);\n"
                "    border-radius: 10px;\n"
                "};\n"
                "\n"
                "background-color: rgb(242, 242, 242);")
            )
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 40, 71, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Megrim"))
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(330, 430, 209, 60))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.installBtn = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.installBtn.sizePolicy().hasHeightForWidth())
        self.installBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.installBtn.setFont(font)
        self.installBtn.setStyleSheet(
            _fromUtf8("background-color: rgb(85, 153, 255);"))
        self.installBtn.setFlat(False)
        self.installBtn.setObjectName(_fromUtf8("installBtn"))
        self.horizontalLayout.addWidget(self.installBtn)
        self.cancelBtn = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cancelBtn.sizePolicy().hasHeightForWidth())
        self.cancelBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setStyleSheet(
            _fromUtf8("background-color: rgb(179, 179, 179);"))
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 70, 511, 341))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget1)
        self.label.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(14)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.label_2.raise_()
        self.label.raise_()

        self.label_3.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cancelBtn.clicked.connect(self.close)
        self.checkItemsDeveloper = [
            "PyCharm", "Sublime Text", "Android IDE", "Atom"]
        self.checkItemsCommom = [
            "VLC", "Chrome", "PopCornTime", "LibreOffice"]
        self.__lst_boxes_Developer()
        self.__lst_boxes_Commom()

    def retranslateUi(self, MainWindow):
        self.label_3.setText(_translate("MainWindow", "Ubuntu", None))
        self.label_4.setText(_translate("MainWindow", "Startup", None))
        self.installBtn.setText(_translate("MainWindow", "Install", None))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel", None))
        self.label.setText(_translate("MainWindow", "Developer", None))
        self.label_2.setText(_translate("MainWindow", "Commom", None))

    def __include_program(self, item):
        if item.checkState:
            print(item.text())
        else:
            pass

    def __lst_boxes_Developer(self):
        self.listView = QtGui.QListView(parent=None)
        model = QtGui.QStandardItemModel()
        for checkItem in self.checkItemsDeveloper:
            item = QtGui.QStandardItem()
            item.setText(checkItem)
            item.setCheckable(True)
            item.setSelectable(False)
            item.setEditable(False)
            model.appendRow(item)
        model.itemChanged.connect(self.__include_program)
        self.listView.setModel(model)
        self.verticalLayout.addWidget(self.listView)

    def __lst_boxes_Commom(self):
        self.listView = QtGui.QListView(parent=None)
        model = QtGui.QStandardItemModel()
        for checkItem in self.checkItemsCommom:
            item = QtGui.QStandardItem()
            item.setText(checkItem)
            item.setCheckable(True)
            item.setSelectable(False)
            item.setEditable(False)
            model.appendRow(item)
        model.itemChanged.connect(self.__include_program)
        self.listView.setModel(model)
        self.verticalLayout_2.addWidget(self.listView)

    def close(self):
        choice = QtGui.QMessageBox.question(
            None,
            "Exit", "Are you sure?!",
            QtGui.QMessageBox.Yes,
            QtGui.QMessageBox.No
        )
        if choice == QtGui.QMessageBox.Yes:
            print("Closing the application ...")
            sys.exit()
        else:
            pass


def run():

    app = QtGui.QApplication(sys.argv)
    win = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
