from enum import Enum;
import random;

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    PRINCESS = 4
    PRINCE = 5
    EMPTY = 6


class Square:
    def __init__(self, type_of, value = False):
        self.type_of = type_of
        self.selected_v = value

    @property
    def type(self):  # Чтение
        return self.type

    @type.setter
    def type(self, value):  # Запись
        self.type = value

    @property
    def selected(self):  # Чтение
        return self.selected_v

    @selected.setter
    def selected(self, value):  # Запись
        self.selected_v = value


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = []
        self.create_matrix()


    def create_matrix(self):
        for r in range(self.height): #строки
            self.matrix.append([]) # создаем пустую строку
            for c in range(self.width): # в каждой строке - 10 элементов
                self.matrix[r].append(Square(Color(random.randint(1,3)))) # добавляем очередной элемент в строку
        x = int(random.randint(0, self.width-1))
        self.matrix[int(random.randint(0, 3))][x] = Square(Color.PRINCE)
        self.matrix[int(self.height - 1 - random.randint(0, 3))][x] = Square(Color.PRINCESS)

    def define_unworkable_square(self, x, y):
        self.matrix[y][x] = -1


    def move_define_cheak(self):
        prince = 0
        princess = 0
        for r in range(self.height):
            for c in range(self.width):
                if self.matrix[r][c].type_of == Color.EMPTY:
                    for i in range(r, 1, -1):
                        self.matrix[i][c] = self.matrix[i-1][c]
                    self.matrix[0][c] = Color(random.randint(1,3))
                if self.matrix[r][c].type_of == Color.PRINCE:
                    prince = r
                if self.matrix[r][c].type_of == Color.PRINCESS:
                    princess = r
        if princess - prince == 1:
            return True
        else:
            return False

    

