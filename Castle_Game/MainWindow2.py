import math
from Castle2 import *
from ItemManager import *
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import QModelIndex, Qt, QTimer, QTime
from PyQt5.QtWidgets import QTableWidgetItem, QMainWindow, QMessageBox
from MainWindowUI import Ui_MainWindow as MainWindowUI

class MainWindow(QMainWindow, MainWindowUI):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.SelectBttn.clicked.connect(self.selected_bttn_clicked)
        self.RestartBttn.clicked.connect(self.restart_bttn_clicked)
        self.rulesBttn.clicked.connect(self.show_rules)
        self.GameFieldTW.setColumnCount(5)
        self.GameFieldTW.setRowCount(9)

        def new_mouse_press_event(e: QMouseEvent) -> None:
            idx = self.GameFieldTW.indexAt(e.pos())
            self.on_item_clicked(idx, e)
        self.GameFieldTW.mousePressEvent = new_mouse_press_event
        self.item_manager = ItemManager()
        self.init_game_field()



    def timerEvent(self):
        self.time = self.time.addSecs(1)
        self.Lb2.setText(self.game.calculate_the_time(self.time.second() + self.time.minute()*60))
        if self.game.failed:
            self.game_is_over.setText("You failed")
            self.timer.stop()


    def show_rules(self):
        self.timer.stop()
        data = ""
        with open("rules.html", 'r', encoding='utf-8') as inf:
            for string in inf:
                data += string
        reply = QMessageBox.information(self, "Rules", data, QMessageBox.Ok);
        if reply == QMessageBox.Ok and not(self.game.game_is_over or self.game.failed):
            self.timer.start(1000)

    def init_game_field(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(1000)
        self.time = QTime(0, 0, 0)
        self.game_is_over.setText("")
        self.ScoreLb.setText("0")
        self.game = Game(5, 9)
        self.game.define_unworkable_square(0, 3)
        self.game.define_unworkable_square(4, 3)
        for i in range(self.game.height):
            for j in range(self.game.width):
                self.GameFieldTW.setItem(i, j, QTableWidgetItem())
                type = self.game.matrix[i][j].type_of
                self.GameFieldTW.item(i, j).setBackground(self.item_manager.define_color(type, False))
                self.GameFieldTW.item(i, j).setText(self.item_manager.define_text(type))


    def on_item_clicked(self, e: QModelIndex, me: QMouseEvent = None) -> None:
        if me.button() == Qt.LeftButton:
            self.left_mouse_click(e.row(), e.column())

    def left_mouse_click(self, row, col) -> None:
        if not(self.game.game_is_over or self.game.failed or self.game.matrix[row][col].type_of == Color.UNWORKABLE):
            if not ((row, col) in self.game.selected):
                color = self.item_manager.define_color(self.game.matrix[row][col].type_of, True)
                if self.game.previousClick == None:
                    self.game.previousClick = ((row), int(col))
                    self.game.selected_type = self.game.matrix[row][col].type_of;
                else:
                    if self.game.selected_type != self.game.matrix[row][col].type_of:
                        raise Exception("Последовательность должна состоять из элементов одинакового типа")
                    if math.fabs(self.game.previousClick[0] - row) + math.fabs(self.game.previousClick[1] - int(col)) > 1:
                        raise Exception("Последовательность выделена неверна")
                self.game.selected.append((row, col))
                self.game.previousClick = (row, col)

            else:
                color = self.item_manager.define_color(self.game.matrix[row][col].type_of, False)
                self.game.selected.remove((row, col))
                if len(self.game.selected) == 0:
                    self.game.selected_type = -1
                    self.game.previousClick = None
            self.GameFieldTW.item(row, col).setBackground(color)

    def redraw(self):
        for i in range(self.game.height):
            for j in range(self.game.width):
                type = self.game.matrix[i][j].type_of
                color = self.item_manager.define_color(type, False)
                text = self.item_manager.define_text(type)
                self.GameFieldTW.item(i, j).setBackground(color)
                self.GameFieldTW.item(i, j).setText(text)

    def selected_bttn_clicked(self):
        if not(self.game.game_is_over):
            self.game.mark_in_matrix()
            self.game.move_define_cheak()
            if (self.game.game_is_over):
                self.game_is_over.setText("Game is over")
                self.timer.stop()
            self.redraw()
            self.ScoreLb.setText(str(self.game.score_value))


    def restart_bttn_clicked(self):
        self.init_game_field()

