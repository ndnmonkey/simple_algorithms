import math
def swap(a,b,list):
    z1 = list[a]
    z2 = list[b]
    list[a] = z2
    list[b] =z1
    print(list)

def xier(list):
    list_l = []
    list_r = []
    for i in range(0, math.ceil(len(list) / 2)):
        if (list[len(list) - 1 - i] < list[0]):
            right = len(list)-i-1
            print("right:",right)
            list_r.append(right)
            continue

    for i in range(0, math.ceil(len(list) / 2)):
        if (list[i + 1] > list[0]):
            left = i+1
            print("left",left)
            list_l.append(left)
            continue
    print(list_r,list_l)
    for k in range(0,max(len(list_r),len(list_l))-1):
        swap(list_l[k],list_r[k],list)
        print("k",k)
    swap(0,list_r[k]-1,list)


list = [6,1,2,7,9,3,4,5,10,8]
xier(list)