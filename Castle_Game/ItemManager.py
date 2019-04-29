from Castle2 import Color
from PyQt5 import QtGui


class ItemManager:

    def __init__(self):
        self.type = -1;
        self.text = ""

    def define_color(self, type, selected):
        dif = 60
        if not (selected):
            dif = 0
        if type == Color.BLUE:
            return QtGui.QColor(65, 105, 255 - dif)
        if type == Color.GREEN:
            return QtGui.QColor(152, 251 - dif, 152)
        if type == Color.RED:
            return QtGui.QColor(178 - dif, 34, 34)
        if type == Color.PRINCE:
            return QtGui.QColor(205, 205, 205)
        if type == Color.PRINCESS:
            return QtGui.QColor(235, 155, 235)
        if type == Color.UNWORKABLE:
            return QtGui.QColor(0, 0, 0)

    def define_text(self, type):
        if type == Color.PRINCE:
            return "Prince"
        elif type == Color.PRINCESS:
            return "Princess"
        else:
            return ""
