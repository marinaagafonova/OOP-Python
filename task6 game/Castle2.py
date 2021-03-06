from enum import Enum;
import random;

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    PRINCESS = 4
    PRINCE = 5
    EMPTY = 6


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
                self.matrix[r].append(Color(random.randint(1,3))) # добавляем очередной элемент в строку
        x = int(random.randint(0, self.width))
        self.matrix[int(random.randint(0, 3))][x] = Color.PRINCE
        self.matrix[int(self.height - random.randint(0,3))][x] = Color.PRINCESS

    def define_unworkable_square(self, x, y):
        self.matrix[y][x] = -1


    def move_define_cheak(self):
        prince = 0
        princess = 0
        for r in range(self.height):
            for c in range(self.width):
                if self.matrix[r][c] == Color.EMPTY:
                    for i in range(r, 1, -1):
                        self.matrix[i][c] = self.matrix[i-1][c]
                    self.matrix[0][c] = Color(random.randint(1,3))
                if self.matrix[r][c] == Color.PRINCE:
                    prince = r
                if self.matrix[r][c] == Color.PRINCESS:
                    princess = r
        if princess - prince == 1:
            return True
        else:
            return False

    

