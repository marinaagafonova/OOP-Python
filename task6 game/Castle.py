import random;
from enum import Enum;
import math;

class Color(Enum):
     RED = 1
     GREEN = 2
     BLUE = 3
     PRINCESS = 4
     PRINCE = 5


class Square:
    def __init__(self,type_of_cude, x, y, selected):
        self.type = type_of_cude
        self.x = x
        self.y = y
        self.selected = selected
    
    @property
    def type_of_cude(self):                       # Чтение
        return self.type
    @type_of_cude.setter
    def type_of_cude(self, value):                # Запись
        self.type = value
    
    @property
    def x(self):                       # Чтение
        return self.x
    @x.setter
    def x(self, value):                # Запись
        self.x = value

    @property
    def y(self):                       # Чтение
        return self.y
    @y.setter
    def y(self, value):                # Запись
        self.y = value

    @property
    def selected(self):                       # Чтение
        return self.selected
    @selected.setter
    def selected(self, value):                # Запись
        self.selected = value


class Game:
    
    def __init__(self):
        self.width = 4
        self.height = 8
        self.squares = []
    
    @property
    def width(self):                       # Чтение
        return self.width

    @property
    def height(self):                       # Чтение
        return self.height
    
    def start(self):
        squares = []
        #define prince & princess
        princess = Square(Color.PRINCESS, 0, 0, False)
        prince = Square(Color.PRINCE, 0, 0, False)
        x = random.randint(0, self.width)
        prince.x = x
        princess.x = x
        prince.y = 0 + random.randint(0, 3)
        princess.y = self.height - random.randint(0,3)
        squares.append(prince)
        squares.append(princess)
        #Color(num)
        for i in range(self.height + 1):
            for j in range(self.width + 1):
                if j != x and i != prince.y and i != princess.y:
                    squares.append(Color(random.randint(1,3)), j, i, False)
        self.squares = squares
        return squares

    def find_min_and_max_X(self, selected):
        minX = self.width
        maxX = 0
        for square in selected:
            if (square.x > maxX):
                maxX = square.x
            if (square.x < minX):
                minX = square.x
        return minX, maxX

    def find_min_and_max_Y(self, selected, x):
        maxY = 0
        minY = self.height
        for square in selected:
            if (square.x == x):
                if(square.y < minY):
                    minY = square.y
                if square.y > maxY:
                    maxY = square.y
        return minY, maxY

    def remove_selected(self, selected):
        for el in selected:
            self.squares.remove(el)

    def move_squares(self, x, dif, maxY):
        minY = self.height
        for el in self.squares:
            if el.x == x and el.y < maxY:
                el.y += dif
                if el.y < minY:
                    minY = el.y

    def add_new(self, minY, x):
        for i in range(minY):
            self.squares.append(Color(random.randint(1,3)), x, i, False)


    def process_selected(self, selected):
        try:
            if(self.check_selected(selected)):
                minX, maxX = self.find_min_and_max_X(selected)
                for j in range(minX, maxX+1):
                    minY, maxY = self.find_min_and_max_Y(selected, j)
                    dif = math.fabs(maxY - minY) + 1
                    self.move_squares(j, dif, maxY)
                    self.add_new(minY, j)
                self.remove_selected(selected)
                return self.squares
        except Exception as e:
            return e;    
    

    def check_if_game_is_over(self):
        princess = Square(Color.PRINCESS, 0, 0, False)
        prince = Square(Color.PRINCE, 0, 0, False)
        for el in self.squares:
            if(el.type == Color.PRINCE):
                prince = el
            if el.type == Color.PRINCESS:
                princess = el
        if princess.y - prince.y == 1:
            return True
        return False

    def check_selected(self, selected):
        if len(selected) <= 2:
            raise Exception("Последовательность должна состоять больше, чем из двух элементов")

        current_type = selected[0]
        for square in selected:
            if current_type != square.type:
                raise Exception("Последовательность должна состоять из элементов одинакового типа")

        for i in range(1, len(selected)):
            if math.fabs(selected[i].x - selected[i-1].x) + math.fabs(selected[i].y - selected[i-1].y) != 1:
                raise Exception("Последовательность выделена неверна")
        return True
        

