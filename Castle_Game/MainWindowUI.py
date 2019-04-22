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
        self.SelectBttn = QtGui.QPushButton(self.centralwidget)
        self.SelectBttn.setGeometry(QtCore.QRect(30, 60, 75, 23))
        self.SelectBttn.setObjectName(_fromUtf8("SelectBttn"))
        self.RestartBttn = QtGui.QPushButton(self.centralwidget)
        self.RestartBttn.setGeometry(QtCore.QRect(30, 30, 75, 23))
        self.RestartBttn.setObjectName(_fromUtf8("RestartBttn"))
        self.GameFieldTW = QtGui.QTableWidget(self.centralwidget)
        self.GameFieldTW.setGeometry(QtCore.QRect(130, 20, 451, 601))
        self.GameFieldTW.setObjectName(_fromUtf8("GameFieldTW"))
        self.GameFieldTW.setColumnCount(0)
        self.GameFieldTW.setRowCount(0)
        self.GameFieldTW.horizontalHeader().setMinimumSectionSize(19)
        self.game_is_over = QtGui.QLabel(self.centralwidget)
        self.game_is_over.setGeometry(QtCore.QRect(40, 100, 46, 13))
        self.game_is_over.setText(_fromUtf8(""))
        self.game_is_over.setObjectName(_fromUtf8("game_is_over"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 140, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.ScoreLb = QtGui.QLabel(self.centralwidget)
        self.ScoreLb.setGeometry(QtCore.QRect(40, 160, 46, 13))
        self.ScoreLb.setObjectName(_fromUtf8("ScoreLb"))
        self.Lb2 = QtGui.QLabel(self.centralwidget)
        self.Lb2.setGeometry(QtCore.QRect(40, 200, 46, 13))
        self.Lb2.setObjectName(_fromUtf8("Lb2"))
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
        self.label.setText(_translate("MainWindow", "Score", None))
        self.ScoreLb.setText(_translate("MainWindow", "0", None))
        self.Lb2.setText(_translate("MainWindow", "Time", None))

