import math;

from MainWindowUI import Ui_MainWindow as MainWindowUI
from Castle2 import *

from PyQt5 import QtSvg
from PyQt5.QtGui import QMouseEvent, QPainter, QStandardItemModel
from PyQt5.QtWidgets import QMainWindow, QItemDelegate, QStyleOptionViewItem
from PyQt5.QtCore import QModelIndex, QRectF, Qt


from PyQt5 import QtGui;

from PyQt5.QtWidgets import QApplication, QTableView, QPushButton, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt

class MainWindow1(QMainWindow, MainWindowUI):
    # Переопределяем конструктор класса
    def __init__(self):
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(608, 684))
        self.previousClick = 0
        self.selected = []
        selectBtn = QPushButton('Select', self)
        selectBtn.move(10,10)
        restartBtn = QPushButton('Restart', self)
        restartBtn.move(30, 30)

        central_widget = QWidget(self)  # Создаём центральный виджет
        self.setCentralWidget(central_widget)  # Устанавливаем центральный виджет
        grid_layout = QGridLayout()  # Создаём QGridLayout
        central_widget.setLayout(grid_layout)  # Устанавливаем данное размещение в центральный виджет
        self.table = QTableView(self)
        self.table.setGeometry(30, 30, 580, 660)
        self.model = QtGui.QStandardItemModel(5, 3, self)
        self.game = Game(5,9)
        for i in range(self.game.height):
            for j in range(self.game.width):
                self.model.setItem(i, j, QtGui.QStandardItem())
                color = self.define_color(self.game.matrix[i][j])
                self.model.item(i, j).setBackground(color)
        self.table.setModel(self.model)
        grid_layout.addWidget(selectBtn, 0, 0)
        grid_layout.addWidget(restartBtn,1,0)
        grid_layout.addWidget(self.table, 0, 1)  # Добавляем таблицу в сетку

        def new_mouse_press_event(e: QMouseEvent) -> None:
            idx = self.table.indexAt(e.pos())
            self.on_item_clicked(idx, e)
        self.table.mousePressEvent = new_mouse_press_event


    def init_game_field(self):
        self.game = Game(5,9)
        for i in range(self.game.height):
            for j in range(self.game.width):
                self.table.setItem(i, j, QTableWidgetItem())
                color = self.define_color(self.game.matrix[i][j])
                self.table.item(i, j).setBackground(color)

    def define_color(self, color):
        if color == Color.BLUE:
            return QtGui.QColor(0,0,255)
        if color == Color.GREEN:
            return QtGui.QColor(0,255,0)
        if color == Color.RED:
            return QtGui.QColor(255,0,0)
        if color == Color.PRINCE:
            return QtGui.QColor(205,205,205)
        if color == Color.PRINCESS:
            return QtGui.QColor(235,155,235)

    def on_item_clicked(self, e: QModelIndex, me: QMouseEvent = None) -> None:
        if me.button() == Qt.LeftButton:
            self.left_mouse_click(e.row(), e.column())


    def left_mouse_click(self, row, col) -> None:
        if self.previousClick == 0:
            self.previousClick = [int(row), int(col)]
            #self.table.item(row, col).setFocusPolicy(Qt.NoFocus)
        else:
            if math.fabs(self.previousClick[0] - int(row)) + math.fabs(self.previousClick[1] - int(col)) != 1:
                self.selected = []
                raise Exception("Последовательность выделена неверна")
        self.selected.append([row, col])
        self.previousClick = [int(row), int(col)]

