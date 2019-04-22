import math;
from Castle2 import *
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import QModelIndex, Qt, QTimer, QTime
from PyQt5.QtWidgets import QTableWidgetItem

(MainWindowUI, QMainWindow) = uic.loadUiType('MainWindow.ui')

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = MainWindowUI()
        self.ui.setupUi(self)
        self.ui.SelectBttn.clicked.connect(self.selected_bttn_clicked)
        self.ui.RestartBttn.clicked.connect(self.restart_bttn_clicked)
        self.ui.GameFieldTW.setColumnCount(5)
        self.ui.GameFieldTW.setRowCount(9)
        self.ui.GameFieldTW.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.ui.GameFieldTW.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.ui.GameFieldTW.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.ui.GameFieldTW.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.ui.GameFieldTW.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)


        def new_mouse_press_event(e: QMouseEvent) -> None:
            idx = self.ui.GameFieldTW.indexAt(e.pos())
            self.on_item_clicked(idx, e)
        self.ui.GameFieldTW.mousePressEvent = new_mouse_press_event
        self.init_game_field()
        self.timer = QTimer()
        self.time = QTime(0, 0, 0)
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(1000)

        #self.timer.timeout.connect(self.time)



    def timerEvent(self):
        self.time = self.time.addSecs(1)
        endtime = QTime(0, 1, 37)
        self.ui.Lb2.setText(str(endtime.minute() - self.time.minute()) + ":" + str(endtime.second() - self.time.second()))
        if self.ui.Lb2.text() == "0:0":
            self.ui.game_is_over.setText("Game is over")
            self.timer.stop()

    def init_game_field(self):
        self.time = QTime(0, 0, 0)
        #self.timer.start(1000)
        self.previousClick = 0
        self.selected = []
        self.selected_type = -1
        self.ui.game_is_over.setText("")
        self.ui.ScoreLb.setText("0")
        self.game = Game(5, 9)
        for i in range(self.game.height):
            for j in range(self.game.width):
                self.ui.GameFieldTW.setItem(i, j, QTableWidgetItem())
                if self.game.matrix[i][j].type_of == Color.PRINCE:
                    self.ui.GameFieldTW.item(i, j).setText("Prince")
                if self.game.matrix[i][j].type_of == Color.PRINCESS:
                    self.ui.GameFieldTW.item(i, j).setText("Princess")
                color = self.define_color(self.game.matrix[i][j].type_of)
                self.ui.GameFieldTW.item(i, j).setBackground(color)

    def define_color(self, color, selected=False):
        dif = 60
        if not (selected):
            dif = 0
        if color == Color.BLUE:
            return QtGui.QColor(65, 105, 255 - dif)
        if color == Color.GREEN:
            return QtGui.QColor(152, 251 - dif, 152)
        if color == Color.RED:
            return QtGui.QColor(178 - dif, 34, 34)
        if color == Color.PRINCE:
            return QtGui.QColor(205, 205, 205)
        if color == Color.PRINCESS:
            return QtGui.QColor(235, 155, 235)

    def on_item_clicked(self, e: QModelIndex, me: QMouseEvent = None) -> None:
        if me.button() == Qt.LeftButton:
            self.left_mouse_click(e.row(), e.column())

    def left_mouse_click(self, row, col) -> None:
        if self.ui.game_is_over.text() != "Game is over":
            color = 0
            if not ([row, col] in self.selected):
                # self.table.item(row, col).isSelected = True
                color = self.define_color(self.game.matrix[row][col].type_of, True)
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
                self.selected.remove([row, col])
                if len(self.selected) == 0:
                    self.selected_type = -1
                    self.previousClick = 0
            self.ui.GameFieldTW.item(row, col).setBackground(color)

    def redraw(self):
        for i in range(self.game.height):
            for j in range(self.game.width):
                type = self.game.matrix[i][j].type_of
                color = self.define_color(type)
                self.ui.GameFieldTW.item(i, j).setBackground(color)
                if(type == Color.PRINCE or type == Color.PRINCESS):
                    if type == Color.PRINCE:
                        self.ui.GameFieldTW.item(i, j).setText("Prince")
                    if type == Color.PRINCESS:
                        self.ui.GameFieldTW.item(i, j).setText("Princess")
                else:
                    self.ui.GameFieldTW.item(i, j).setText("")

    def selected_bttn_clicked(self):
        if self.ui.game_is_over.text() != "Game is over":
            self.mark_in_matrix()
            endgame = self.game.move_define_cheak()
            if (endgame):
                self.ui.game_is_over.setText("Game is over")
                self.timer.stop()
            self.redraw()
            self.ui.ScoreLb.setText(str(self.game.score_value))

    def mark_in_matrix(self):
        for elem in self.selected:
            self.game.matrix[elem[0]][elem[1]].type_of = Color.EMPTY
        self.selected = []
        self.selected_type = -1
        self.previousClick = 0

    def restart_bttn_clicked(self):
        self.init_game_field()

