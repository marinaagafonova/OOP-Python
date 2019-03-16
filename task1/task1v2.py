import argparse
import random


def bubble_sort(array):
    l = len(array)
    for i in range(1, l):
        for j in range(l-1, i-1, -1):
            if array[j-1] > array[j]:
                t = array[j-1]
                array[j-1] = array[j]
                array[j] = t
    return array


def copy_array(l, dif):
    l1 = []
    for i in l:
        l1.append(i)
    if(dif<0):
        #l1.sort(reverse = True)
        l1 = bubble_sort(l1)
        l1.reverse()
    else:
        #l1.sort()
        l1 = bubble_sort(l1)
    return l1;


def check_for_correct(i1, i2, l):
    count = 0
    dif = l[i2] - l[i1]
    print("dif = ", dif, end=" ")
    if dif != 0:
        newList = copy_array(l, dif)
        i1 = newList.index(l[i1])
        i2 = newList.index(l[i2])
        for i in range(len(newList)-1):
            if((i!=i1 and i!=i2 or i+1!=i1 and i+1!=i2) and newList[i+1] - newList[i]!=dif):
                count += 1
    else:
        count = -1
    return count


def sort(i1, i2, l):
    dif = l[i2] - l[i1]
    #l = copy_array(l, dif)
    i1 = l.index(l[i1])
    i2 = l.index(l[i2])
    if i1!=0:
        for i in range(i1-1, 0, -1):
            if l[i+1] - l[i] != -dif:
                l[i] = l[i+1] - dif
    for i in range(i1, i2):
        if(i==i1):
            continue
        if(l[i] - l[i-1] != dif):
            l[i] = l[i-1] + dif
    for i in range(i2, len(l)-1):
        if l[i+1] - l[i] != dif:
            l[i+1] = l[i] + dif
    return l


def open_file(filename):
    list = []
    with open(filename) as inf:
        for string in inf:
            temp = string.split()
            for elem in temp:
                list.append(int(elem))
    return list


def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    list = open_file(args.filename)

    counts = {}  # key is count, value is an indexs of a pair
    for i in range(len(list) - 1):
        for j in range(1, len(list)):
            res = check_for_correct(i, j, list)
            print("index = ", i, " ", j, " count = ", res)
            if res != -1:
                if (counts.get(res) == None):
                    counts[res] = (i, j)
    
    min = len(list)
    for key in counts.keys():
        if key < min:
            min = key
    print("min = ", min)
    print("index = ", counts.get(min))
    indexs = counts.get(min)
    print("Исходный массив: ")
    for el in list:
        print(el, end=" ")
    print()
    if(indexs == None):
        print("В списке нет пар, на основе которых можно составить арифметическую прогрессию")
    else:
        list = sort(indexs[0], indexs[1], list)
        print("Результат")
        for el in list:
            print(el, end=" ")
        
        
main()