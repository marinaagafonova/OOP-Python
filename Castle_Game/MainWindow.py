import os

from MainWindowUI import Ui_MainWindow as MainWindowUI
from Castle import *

from PyQt5 import QtSvg
from PyQt5.QtGui import QMouseEvent, QPainter, QStandardItemModel
from PyQt5.QtWidgets import QMainWindow, QItemDelegate, QStyleOptionViewItem
from PyQt5.QtCore import QModelIndex, QRectF, Qt

class MainWindow(QMainWindow, MainWindowUI):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

