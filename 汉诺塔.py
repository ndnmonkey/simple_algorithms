'''把X上的盘子放在Z上'''
def hanoi(n,x,y,z):
    if n == 1:
        print( x + " - > " + z)
    else:
        hanoi(n-1,x,z,y)   #将n-1个盘子从x移动到y
        print(x + " - > " + z)#将最后一个移动到Z上
        hanoi(n-1,y,x,z)#将y上的盘子移动到Z上

hanoi(3,"x","y","z")