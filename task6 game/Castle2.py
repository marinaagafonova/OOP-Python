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
        self.matrix = []
        self.create_matrix(width, height)


    def create_matrix(self, width, height):
        for r in range(height): #строки
            self.matrix.append([]) # создаем пустую строку
            for c in range(width): # в каждой строке - 10 элементов
                self.matrix[r].append(Color(random.randint(1,3))) # добавляем очередной элемент в строку
        x = int(random.randint(0, width))
        self.matrix[int(random.randint(0, 3))][x] = Color.PRINCE
        self.matrix[int(height - random.randint(0,3))][x] = Color.PRINCESS

    def define_unworkable_square(self, x, y):
        self.matrix[y][x] = -1

    

