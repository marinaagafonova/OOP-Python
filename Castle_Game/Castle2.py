from enum import Enum;
import random;

class Color(Enum):
    UNWORKABLE = 0
    RED = 1
    GREEN = 2
    BLUE = 3
    PRINCESS = 4
    PRINCE = 5
    EMPTY = 6

class Square:
    def __init__(self, type_of):
        self.type_of = type_of

    @property
    def type(self):  # Чтение
        return self.type

    @type.setter
    def type(self, value):  # Запись
        self.type = value


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = []
        self.create_matrix()
        self.score = 0
        self.selected = []
        self.previousClick = None
        self.selected_type = -1
        self.game_is_over = False;
        self.failed = False;

    @property
    def score_value(self):  # Чтение
        return self.score

    def create_matrix(self):
        for r in range(self.height): #строки
            self.matrix.append([]) # создаем пустую строку
            for c in range(self.width): # в каждой строке - 10 элементов
                self.matrix[r].append(Square(Color(random.randint(1, 3)))) # добавляем очередной элемент в строку
        x = int(random.randint(1, self.width-2))
        self.matrix[int(random.randint(0, 3))][x] = Square(Color.PRINCE)
        self.matrix[int(self.height - 1 - random.randint(0, 3))][x] = Square(Color.PRINCESS)

    def define_unworkable_square(self, x, y):
        self.matrix[y][x] = Square(Color.UNWORKABLE)


    def move_define_cheak(self):
        prince = 0
        princess = 0
        selected = 0
        for r in range(self.height):
            for c in range(self.width):
                if self.matrix[r][c].type_of == Color.EMPTY:
                    selected += 1
                    last = 0;
                    for i in range(r, 0, -1):
                        if self.matrix[i][c].type_of == Color.UNWORKABLE:
                            last = i+1;
                            break;
                        temp = self.matrix[i-1][c].type_of
                        self.matrix[i][c].type_of = self.matrix[i-1][c].type_of
                    color = Color(random.randint(1, 3))
                    self.matrix[last][c].type_of = color
                if self.matrix[r][c].type_of == Color.PRINCE:
                    prince = r
                if self.matrix[r][c].type_of == Color.PRINCESS:
                    princess = r
        self.refresh_score(selected)
        if princess - prince == 1:
            self.game_is_over = True;
        else:
            self.game_is_over = False;

    def refresh_score(self, selected):
        three = 27
        increase = 6
        four = 48
        dif = four - three
        value = 0
        if(selected == 3 or selected == 4):
            if(selected == 3):
                self.score += three
            if(selected == 4):
                self.score += four
        else:
            for i in range(selected - 4):
                dif += increase
                value += dif
            self.score += value

    def mark_in_matrix(self):
        for elem in self.selected:
            self.matrix[elem[0]][elem[1]].type_of = Color.EMPTY
        self.selected = []
        self.selected_type = -1
        self.previousClick = None

    def calculate_the_time(self, seconds):
        #1:37
        limit_time = 97;
        if limit_time == seconds:
            self.failed = True;
            return "0:0"
        else:
            result_seconds = limit_time - seconds;
            return str(result_seconds//60) + ":" + str(result_seconds%60);

