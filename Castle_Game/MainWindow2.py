from Castle2 import *
from ItemManager import *
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import QModelIndex, Qt, QTimer, QTime
from PyQt5.QtWidgets import QTableWidgetItem, QMainWindow, QMessageBox, QInputDialog
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
        self.actionSize.triggered.connect(self.change_width)
        self.actionHeight.triggered.connect(self.change_height)

        def new_mouse_press_event(e: QMouseEvent) -> None:
            idx = self.GameFieldTW.indexAt(e.pos())
            self.on_item_clicked(idx, e)
        self.GameFieldTW.mousePressEvent = new_mouse_press_event
        self.init_game_field(5, 9)



    def timerEvent(self):
        self.time = self.time.addSecs(1)
        self.game.refresh_time(self.time.second() + self.time.minute() * 60)
        self.Lb2.setText(self.game.time_left)
        if self.game.is_failed:
            self.game_is_over.setText("You failed")
            self.timer.stop()

    def change_height(self):
        n, ok = QInputDialog.getInt(self, "Height", "Value of height", value=self.game.height, min = 9, max = 20)
        self.init_game_field(self.game.width, n)

    def change_width(self):
        n, ok = QInputDialog.getInt(self, "Width", "Value of width", value=self.game.width, min = 5, max = 13)
        self.init_game_field(n, self.game.height)

    def show_rules(self):
        self.timer.stop()
        data = ""
        with open("rules.html", 'r', encoding='utf-8') as inf:
            for string in inf:
                data += string
        reply = QMessageBox.information(self, "Rules", data, QMessageBox.Ok);
        if reply == QMessageBox.Ok and not(self.game.gameIsover or self.game.is_failed):
            self.timer.start(1000)

    def init_game_field(self, width, height):
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(1000)
        self.time = QTime(0, 0, 0)
        self.game_is_over.setText("")
        self.ScoreLb.setText("0")
        self.game = Game(width, height)

        self.GameFieldTW.setColumnCount(width)
        self.GameFieldTW.setRowCount(height)
        for i in range(self.game.height):
            for j in range(self.game.width):
                self.GameFieldTW.setItem(i, j, QTableWidgetItem())
                type = self.game[i, j]
                self.GameFieldTW.item(i, j).setBackground(ItemManager.define_color(type, False))
                self.GameFieldTW.item(i, j).setText(ItemManager.define_text(type))


    def on_item_clicked(self, e: QModelIndex, me: QMouseEvent = None) -> None:
        if me.button() == Qt.LeftButton:
            self.left_mouse_click(e.row(), e.column())

    def left_mouse_click(self, row, col) -> None:
        try:
            type, is_selected = self.game.add_new_selected((row, col))
            color = ItemManager.define_color(type, is_selected)
            self.GameFieldTW.item(row, col).setBackground(color)
        except SameTypeException:
            QMessageBox.information(self, "Exception", "Последовательность должна состоять из элементов одинакового типа", QMessageBox.Ok);
        except WrongSequenceException:
            QMessageBox.information(self, "Exception", "Последовательность выделена неверно", QMessageBox.Ok);
        except WrongDeletingException:
            QMessageBox.information(self, "Exception", "Удалить можно только последний эллент", QMessageBox.Ok);
        except WrongTypeException:
            QMessageBox.information(self, "Exception", "Выделен элемент, который по правилам нельзя выделять", QMessageBox.Ok);

    def redraw(self):
        for i in range(self.game.height):
            for j in range(self.game.width):
                type = self.game[i, j]
                color = ItemManager.define_color(type, False)
                text = ItemManager.define_text(type)
                self.GameFieldTW.item(i, j).setBackground(color)
                self.GameFieldTW.item(i, j).setText(text)

    def selected_bttn_clicked(self):
        if self.game.deleting_allselected_is_possible():
            self.game.mark_in_matrix()
            self.game.move_define_cheak()
            if (self.game.gameIsover):
                self.game_is_over.setText("Game is over")
                self.timer.stop()
            self.redraw()
            self.ScoreLb.setText(str(self.game.score_value))


    def restart_bttn_clicked(self):
        self.init_game_field(self.game.width, self.game.height)

