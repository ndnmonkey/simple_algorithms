def xuanze(list):
    list2 = []
    for index in range(1,len(list)):
        print("第 %d 次排序list,list2分别为：" %index)
        min = list[0]   #最小值
        for i in list:  #这里的i是里面的数值，而不是序号，print(i)可验证
            #print(i)
            if i < min:
                min = i
        #print(list.index(min))   #知道值求位置
        locate = list.index(min)  #最小值的序号
        temp = list[0]        #以下三行是交换
        list[0] = list[locate]
        list[locate] = temp

        print(list)
        list2.append(list[0])
        list.remove(list[0])
        '''当交换位置后的list第一个值被remove出去后，
        此时的list是[56,80,91,20]了，依此类推，这里是
        本算法利用list最好玩的地方，可以少写一个for'''
        print(list2)

    print("最终的list2:")
    list2.append(list[0])
    print(list2)
if __name__ == '__main__':
    list = [56,12,80,91,20,33,89,99]
    xuanze(list)
