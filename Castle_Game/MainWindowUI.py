# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(608, 684)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SelectBttn = QtWidgets.QPushButton(self.centralwidget)
        self.SelectBttn.setGeometry(QtCore.QRect(30, 60, 75, 23))
        self.SelectBttn.setObjectName("SelectBttn")
        self.RestartBttn = QtWidgets.QPushButton(self.centralwidget)
        self.RestartBttn.setGeometry(QtCore.QRect(30, 30, 75, 23))
        self.RestartBttn.setObjectName("RestartBttn")
        self.GameFieldTW = QtWidgets.QTableWidget(self.centralwidget)
        self.GameFieldTW.setGeometry(QtCore.QRect(130, 20, 451, 601))
        self.GameFieldTW.setRowCount(9)
        self.GameFieldTW.setColumnCount(5)
        self.GameFieldTW.setObjectName("GameFieldTW")
        self.GameFieldTW.horizontalHeader().setVisible(False)
        self.GameFieldTW.horizontalHeader().setDefaultSectionSize(35)
        self.GameFieldTW.horizontalHeader().setHighlightSections(True)
        self.GameFieldTW.horizontalHeader().setMinimumSectionSize(35)
        self.GameFieldTW.verticalHeader().setVisible(False)
        self.GameFieldTW.verticalHeader().setHighlightSections(True)
        self.game_is_over = QtWidgets.QLabel(self.centralwidget)
        self.game_is_over.setGeometry(QtCore.QRect(20, 100, 60, 13))
        self.game_is_over.setText("")
        self.game_is_over.setObjectName("game_is_over")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 140, 46, 13))
        self.label.setObjectName("label")
        self.ScoreLb = QtWidgets.QLabel(self.centralwidget)
        self.ScoreLb.setGeometry(QtCore.QRect(40, 160, 46, 13))
        self.ScoreLb.setObjectName("ScoreLb")
        self.Lb2 = QtWidgets.QLabel(self.centralwidget)
        self.Lb2.setGeometry(QtCore.QRect(40, 200, 46, 13))
        self.Lb2.setObjectName("Lb2")
        self.rulesBttn = QtWidgets.QPushButton(self.centralwidget)
        self.rulesBttn.setGeometry(QtCore.QRect(30, 0, 75, 23))
        self.rulesBttn.setObjectName("rulesBttn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 608, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SelectBttn.setText(_translate("MainWindow", "Select"))
        self.RestartBttn.setText(_translate("MainWindow", "Restart"))
        self.label.setText(_translate("MainWindow", "Score"))
        self.ScoreLb.setText(_translate("MainWindow", "0"))
        self.Lb2.setText(_translate("MainWindow", "Time"))
        self.rulesBttn.setText(_translate("MainWindow", "Rules"))

