# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
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
        MainWindow.resize(608, 684)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(240, 10, 350, 630))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.SelectBttn = QtGui.QPushButton(self.centralwidget)
        self.SelectBttn.setGeometry(QtCore.QRect(40, 90, 75, 23))
        self.SelectBttn.setObjectName(_fromUtf8("SelectBttn"))
        self.RestartBttn = QtGui.QPushButton(self.centralwidget)
        self.RestartBttn.setGeometry(QtCore.QRect(40, 60, 75, 23))
        self.RestartBttn.setObjectName(_fromUtf8("RestartBttn"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 608, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.SelectBttn.setText(_translate("MainWindow", "Select", None))
        self.RestartBttn.setText(_translate("MainWindow", "Restart", None))

