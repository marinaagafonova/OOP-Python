from enum import Enum
import random
import math

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
        self.__type_of = type_of

    @property
    def type(self):  # Чтение
        return self.__type_of

    @type.setter
    def type(self, value):  # Запись
        self.__type_of = value


class SameTypeException(Exception):
    pass


class WrongSequenceException(Exception):
    pass


class WrongDeletingException(Exception):
    pass


class WrongTypeException(Exception):
    pass


class Game:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__matrix = []
        self.__create_matrix()
        self.__score = 0
        self.__selected = []
        self.__previousClick = None
        self.__selected_type = -1
        self.__game_is_over = False;
        self.__failed = False;
        self.__time_left = ""

    def __getitem__(self, pos):
        i, j = pos
        return self.__matrix[i][j].type

    @property
    def time_left(self):  # Чтение
        return self.__time_left

    @property
    def score_value(self):  # Чтение
        return self.__score

    @property
    def is_failed(self):  # Чтение
        return self.__failed

    @property
    def gameIsover(self):  # Чтение
        return self.__game_is_over

    @property
    def gameIsover(self):  # Чтение
        return self.__game_is_over

    @property
    def width(self):  # Чтение
        return self.__width

    @property
    def height(self):  # Чтение
        return self.__height

    def __create_matrix(self):
        for r in range(self.height): #строки
            self.__matrix.append([]) # создаем пустую строку
            for c in range(self.__width): # в каждой строке - 10 элементов
                self.__matrix[r].append(Square(Color(random.randint(1, 3)))) # добавляем очередной элемент в строку
        x = int(random.randint(1, self.width-2))
        self.__matrix[int(random.randint(0, 3))][x] = Square(Color.PRINCE)
        self.__matrix[int(self.height - 1 - random.randint(0, 3))][x] = Square(Color.PRINCESS)
        self.__define_unworkable_square(0, 3)
        self.__define_unworkable_square(self.__width - 1, 3)

    def __define_unworkable_square(self, x, y):
        self.__matrix[y][x] = Square(Color.UNWORKABLE)


    def move_define_cheak(self):
        prince = 0
        princess = 0
        selected = 0
        for r in range(self.height):
            for c in range(self.width):
                if self.__matrix[r][c].type == Color.EMPTY:
                    selected += 1
                    last = 0;
                    for i in range(r, 0, -1):
                        if self.__matrix[i][c].type == Color.UNWORKABLE:
                            last = i+1;
                            break;
                        temp = self.__matrix[i-1][c].type
                        self.__matrix[i][c].type = self.__matrix[i-1][c].type
                    color = Color(random.randint(1, 3))
                    self.__matrix[last][c].type = color
                if self.__matrix[r][c].type == Color.PRINCE:
                    prince = r
                if self.__matrix[r][c].type == Color.PRINCESS:
                    princess = r
        self.__refresh_score(selected)
        if princess - prince == 1:
            self.__game_is_over = True;
        else:
            self.__game_is_over = False;

    def __refresh_score(self, selected):
        three = 27
        increase = 6
        four = 48
        dif = four - three
        value = 0
        if(selected == 3 or selected == 4):
            if(selected == 3):
                self.__score += three
            if(selected == 4):
                self.__score += four
        else:
            for i in range(selected - 4):
                dif += increase
                value += dif
            self.__score += value


    def check_for_correct(self, pos):
        i, j = pos
        if self.gameIsover or self.is_failed or self.__matrix[i][j].type == Color.UNWORKABLE or self.__matrix[i][j].type == Color.PRINCE or self.__matrix[i][j].type == Color.PRINCESS:
            return False
        return True

    def __check_if_selected(self, pos):
        return pos in self.__selected

    def __check_if_lastSelected(self, pos):
        return pos == self.__selected[len(self.__selected) - 1]

    def add_new_selected(self, pos):
        i, j = pos
        if self.check_for_correct(pos):
            if not(self.__check_if_selected(pos)):
                if self.__previousClick == None:
                    self.__previousClick = (i, j)
                    self.__selected_type = self.__matrix[i][j].type;
                else:
                    if self.__selected_type != self.__matrix[i][j].type:
                        raise SameTypeException(Exception)
                    if math.fabs(self.__previousClick[0] - i) + math.fabs(
                            self.__previousClick[1] - int(j)) > 1:
                        raise WrongSequenceException(Exception)
                self.__selected.append((i, j))
                self.__previousClick = (i, j)
                return (self.__matrix[i][j].type, True)
            else:
                if self.__check_if_lastSelected(pos):
                    self.__selected.remove((i, j))
                    if len(self.__selected) == 0:
                        self.__selected_type = -1
                        self.__previousClick = None
                    return (self.__matrix[i][j].type, False)
                else:
                    raise WrongDeletingException(Exception)
        else:
            raise WrongTypeException(Exception)


    def mark_in_matrix(self):
        for elem in self.__selected:
            self.__matrix[elem[0]][elem[1]].type = Color.EMPTY
        self.__selected = []
        self.__selected_type = -1
        self.__previousClick = None

    def refresh_time(self, seconds):
        self.__calculate_the_time(seconds)

    def __calculate_the_time(self, seconds):
        #1:37
        limit_time = 97;
        if limit_time == seconds:
            self.failed = True;
            return "0:0"
        else:
            result_seconds = limit_time - seconds;
            self.__time_left = str(result_seconds//60) + ":" + str(result_seconds%60)

    def deleting_allselected_is_possible(self):
        return not(self.gameIsover) and len(self.__selected) > 2

