import argparse
import re

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        return ("(" + str(self.x) + ',' + str(self.y) + ")")


class Triangle:
    def __init__(self, points):
        self.points = points

    def print_triangle(self):
        for point in self.points:
            print(point.print_point(), end=";")

    def belong_to_line(self, p1, p2, p3):
        return (p3.x-p1.x)*(p2.y - p1.y) - (p3.y - p1.y)*(p2.x - p1.x) == 0 and (p1.x < p3.x < p2.x or p2.x < p3.x < p1.x)

    def check_for_line(self):
        if self.belong_to_line(self.points[0], self.points[1], self.points[2]):
            return True
        if self.belong_to_line(self.points[1], self.points[2], self.points[0]):
            return True
        if self.belong_to_line(self.points[0], self.points[2], self.points[1]):
            return True
        return False

    def check_for_correct(self):
        nullX = True
        nullY = True

        for i in range(len(self.points)):
            if (self.points[i].x != 0):
                nullX = False
                break
        for i in range(len(self.points)):
            if (self.points[i].y != 0):
                nullY = False
                break
        if (nullX or nullY):
            return False

        if self.check_for_line():
            return False
        return True

    def check_for_one_quarter(self):
        result = False
        if self.points[0].x * self.points[1].x >= 0 and self.points[0].y * self.points[1].y >= 0:
            if self.points[1].x * self.points[2].x >= 0 and self.points[1].y * self.points[2].y >= 0:
                if self.points[0].x * self.points[2].x >= 0 and self.points[0].y * self.points[2].y >= 0:
                    result = True
        return result


class MyIterTriangle:
    
    def __init__(self, start, end, array):
        self.index = start
        self.end = end
        self.values = array #don't know if it's correct
    
    def __iter__(self):
        result = []
        while True:
            try:
                item = next(self)
                if(item.check_for_correct() and item.check_for_one_quarter()):
                    result.append(item)
            except StopIteration:
                break
        self.data = result
        return self

    def __next__(self):
        if self.index >= self.end:
            raise StopIteration
        current = self.values[self.index] #don't know if it's correct
        self.index += 1
        return current
'''
    def check_for_correct(self):
        nullX = True
        nullY = True

        for i in range(len(self.points)):
            if (self.points[i].x != 0):
                nullX = False
                break
        for i in range(len(self.points)):
            if (self.points[i].y != 0):
                nullY = False
                break
        if (nullX or nullY):
            return False

        if self.check_for_line():
            return False
        return True


    def check_for_one_quarter(self):
        result = False
        if (self.points[0].x * self.points[1].x >= 0 and self.points[0].y * self.points[1].y >= 0):
            if (self.points[1].x * self.points[2].x >= 0 and self.points[1].y * self.points[2].y >= 0):
                if (self.points[0].x * self.points[2].x >= 0 and self.points[0].y * self.points[2].y >= 0):
                    result = True
        return result
'''

class IterTriangles:

    def __init__(self, start, end, array):
        self.index = start
        self.end = end
        self.values = array 

    def __iter__(self):
        result = []
        while True:
            try:
                item = next(self)
                if(item.check_for_correct() and item.check_for_one_quarter()):
                    result.append(item)
            except StopIteration:
                break
        self.values = result
        return iter(self.values)


    def __next__(self):
        if self.index >= self.end:
            raise StopIteration
        current = self.values[self.index]
        self.index += 1
        return current




def accepts(func):
    def wrapper(arg):
        print(arg)
        result = re.match('.+[.]txt$', arg)
        if result == None:
            raise TypeError("Неверный формат файла")
            #return "Неверный формат файла"
        else:
            return func(arg)
    return wrapper


@accepts
def open_file(filename):
    triangles = []
    with open(filename) as inf:
        for string in inf:
            temp = string.split(';')
            for i in range(len(temp)):
                temp[i] = temp[i][1:-1]
            # print(temp[i])
            points = []
            for el in temp:
                coor = el.split(",")
                if len(coor) > 1:
                    points.append(Point(int(coor[0]), int(coor[1])))
            triangles.append(Triangle(points))
    return triangles


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    #args = parser.parse_args()
    
    triangles = open_file(".\input.txt")
    #triangles = open_file(str(args.filename))
    print("Входные данные: \n")
    for i in triangles:
        i.print_triangle()
        print()
    print()
    triangles = IterTriangles(0, len(triangles), triangles)
    print("Results: ")
    tr = triangles
    for item in tr:
        item.print_triangle()
        print()

    '''
    for i in triangles.data:
        if i.check_for_correct() and i.check_for_one_quarter():
            print("Index of triangle = ", str(triangles.data.index(i)))
            i.print_triangle()
            print()
            '''

'''
def open_file(filename):
    triangles = []
    with open(filename) as inf:
        for string in inf:
            temp = string.split(';')
            for i in range(len(temp)):
                temp[i] = temp[i][1:-1]
            # print(temp[i])
            points = []
            for el in temp:
                coor = el.split(",")
                if (len(coor) > 1):
                    points.append(Point(int(coor[0]), int(coor[1])))
            triangles.append(Triangle(points))
    return triangles
'''

main()