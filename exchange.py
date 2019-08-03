import math


def swap(a, b, list):
    z1 = list[a]
    z2 = list[b]
    list[a] = z2
    list[b] = z1
    print(list)


list1 = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
swap(0,9, list1)
