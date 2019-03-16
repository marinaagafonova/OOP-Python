'''
def require_arguments(*reqargs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in reqargs:
                if not arg in kwargs:
                    raise TypeError("Missing %s" % arg)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@require_arguments("N", "p")
def g(x,*args,**kwargs):
    print(x)
	
	
	
	
	
	
	
	
	
def print_input(func):
    def wrapped(*args):
        print("Triangles:")
        func(args)
    return wrapped


@print_input
def triagles_sout(triangles):
    for i in triangles:
        for point in i.points:
            print(point.print_point(), end=";")
        print()

'''
import re
import argparse

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

'''
def accepts(func):
    def wrapper(arg):
        print(arg)
        result = re.match('\w+\.txt$', arg)
        if result == None:
            return "Неверный формат файла"
        else:
            return func(arg)
    return wrapper

'''
def accepts(type):
    def wrapper(f):
        def new_f(*args, **kwds):
            for (a, t) in zip(args, type):
                assert isinstance(a, t), \
                       "arg %r does not match %s" % (a,t)
            return f(*args, **kwds)
        new_f.func_name = f.func_name
        return new_f
    return wrapper
	
	
	#'\w+\.txt$'
	'''

@accepts
def open_file(filename):
    #triangles = []
    input = []
    with open(filename) as inf:
        for string in inf:
            input.append(string)
            '''
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
			'''
	
    return input


parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()
input = open_file(str(args.filename))
#print(str(args.filename))
print(input)