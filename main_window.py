# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ubuntu_startup.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
                "QGroupBox {\n"
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
        self.groupBox = QtGui.QGroupBox(self.widget1)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.widget2 = QtGui.QWidget(self.groupBox)
        self.widget2.setGeometry(QtCore.QRect(10, 20, 105, 80))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.checkBox = QtGui.QCheckBox(self.widget2)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_3.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(self.widget2)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout_3.addWidget(self.checkBox_2)
        self.checkBox_3 = QtGui.QCheckBox(self.widget2)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.verticalLayout_3.addWidget(self.checkBox_3)
        self.verticalLayout.addWidget(self.groupBox)
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
        self.groupBox_2 = QtGui.QGroupBox(self.widget1)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(
            self.cancelBtn, QtCore.SIGNAL(
                _fromUtf8("clicked(bool)")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.label_3.setText(_translate("MainWindow", "Ubuntu", None))
        self.label_4.setText(_translate("MainWindow", "Startup", None))
        self.installBtn.setText(_translate("MainWindow", "Install", None))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel", None))
        self.label.setText(_translate("MainWindow", "Developer", None))
        self.checkBox.setText(_translate("MainWindow", "Sublime Text", None))
        self.checkBox_2.setText(_translate("MainWindow", "Atom", None))
        self.checkBox_3.setText(_translate("MainWindow", "PyCharm", None))
        self.label_2.setText(_translate("MainWindow", "Commom", None))
