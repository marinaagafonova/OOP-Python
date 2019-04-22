import os
import sys;
import math;

from MainWindowUI import Ui_MainWindow as MainWindowUI
from Castle2 import *

from PyQt5 import QtSvg
from PyQt5.QtGui import QMouseEvent, QPainter, QStandardItemModel
from PyQt5.QtWidgets import QMainWindow, QItemDelegate, QStyleOptionViewItem
from PyQt5.QtCore import QModelIndex, QRectF, Qt


from PyQt5 import QtGui;

from PyQt5.QtWidgets import QLabel, QApplication, QTableView, QPushButton, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt


class MainWindow(QMainWindow, MainWindowUI):
    # Переопределяем конструктор класса
    def __init__(self):
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(608, 684))
        self.previousClick = 0
        self.selected = []
        self.selected_type = -1;

        selectBtn = QPushButton('Select', self)
        selectBtn.move(10,10)
        restartBtn = QPushButton('Restart', self)
        restartBtn.move(30, 30)
        self.gameoverLB = QLabel()

        central_widget = QWidget(self)  # Создаём центральный виджет
        self.setCentralWidget(central_widget)  # Устанавливаем центральный виджет
        grid_layout = QGridLayout()  # Создаём QGridLayout
        central_widget.setLayout(grid_layout)  # Устанавливаем данное размещение в центральный виджет
        self.table = QTableWidget(self)  # Создаём таблицу
        self.table.setColumnCount(5)  # Устанавливаем три колонки
        self.table.setRowCount(9)  # и одну строку в таблице
        # заполняем первую строку

        selectBtn.clicked.connect(self.selected_bttn_clicked)
        style = ''' 
        QTableWidget::item {border-style: outset;
        border-width: 3px; border-radius: 7px; border-color: black}
        QTableWidget::item:selected { border-width: 5px; border-radius: 7px; border-color: blue
        }
        '''

        '''
        self.table.setItem(0, 0, QTableWidgetItem("Text in column 1"))
        self.table.setItem(0, 1, QTableWidgetItem("Text in column 2"))
        self.table.setItem(0, 2, QTableWidgetItem("Text in column 3"))
        self.table.setItem(1,0, QTableWidgetItem())
        self.table.item(1,0).setBackground(QtGui.QColor(255,0,0))
        '''
        #self.table.setStyleSheet(style)
        self.init_game_field()
        grid_layout.addWidget(selectBtn, 0, 0)
        grid_layout.addWidget(restartBtn, 1, 0)
        grid_layout.addWidget(self.gameoverLB, 2,0)
        grid_layout.addWidget(self.table, 2, 1)  # Добавляем таблицу в сетку


        def new_mouse_press_event(e: QMouseEvent) -> None:
            idx = self.table.indexAt(e.pos())
            self.on_item_clicked(idx, e)
        self.table.mousePressEvent = new_mouse_press_event


    def init_game_field(self):
        self.game = Game(5,9)
        for i in range(self.game.height):
            for j in range(self.game.width):
                self.table.setItem(i, j, QTableWidgetItem())
                color = self.define_color(self.game.matrix[i][j].type_of)
                self.table.item(i, j).setBackground(color)

    def define_color(self, color, selected = False):
        dif = 60
        if not(selected):
            dif = 0
        if color == Color.BLUE:
            return QtGui.QColor(50, 100, 255-dif)
        if color == Color.GREEN:
            return QtGui.QColor(135, 255-dif, 135)
        if color == Color.RED:
            return QtGui.QColor(255 - dif, 50, 50)
        if color == Color.PRINCE:
            return QtGui.QColor(205, 205, 205)
        if color == Color.PRINCESS:
            return QtGui.QColor(235, 155, 235)

    def on_item_clicked(self, e: QModelIndex, me: QMouseEvent = None) -> None:
        if me.button() == Qt.LeftButton:
            self.left_mouse_click(e.row(), e.column())


    def left_mouse_click(self, row, col) -> None:
        color = 0
        if not(self.game.matrix[row][col].selected):
            #self.table.item(row, col).isSelected = True
            color = self.define_color(self.game.matrix[row][col].type_of, True)
            self.game.matrix[row][col].selected = True
            if self.previousClick == 0:
                self.previousClick = [int(row), int(col)]
                self.selected_type = self.game.matrix[row][col].type_of;
            else:
                if self.selected_type != self.game.matrix[row][col].type_of:
                    raise Exception("Последовательность должна состоять из элементов одинакового типа")
                if math.fabs(self.previousClick[0] - int(row)) + math.fabs(self.previousClick[1] - int(col)) > 1:
                    self.selected = []
                    raise Exception("Последовательность выделена неверна")
            self.selected.append([row, col])
            self.previousClick = [int(row), int(col)]

        else:
            color = self.define_color(self.game.matrix[row][col].type_of)
            self.game.matrix[row][col].selected = False
            self.selected.remove([row, col])
            if len(self.selected) == 0:
                self.selected_type = -1
                self.previousClick = 0
        self.table.item(row, col).setBackground(color)

    def redraw(self):
        for i in range(self.game.height):
            for j in range(self.game.width):
                color = self.define_color(self.game.matrix[i][j].type_of)
                self.table.item(i, j).setBackground(color)

    def selected_bttn_clicked(self):
        for elem in self.selected:
            self.game.matrix[elem[0]][elem[1]].type_of = Color.EMPTY
        endgame = self.game.move_define_cheak()
        if(endgame):
            self.gameoverLB.setText("Game is over")
        self.redraw()
        self.selected = []
        self.selected_type = -1
        self.previousClick = 0


