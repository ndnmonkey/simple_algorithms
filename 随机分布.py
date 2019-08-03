import random
import matplotlib.pyplot as plt

def random_list(start,stop,length):
    jishu = 50  #基数的意思或作为迭代次数，不是灵活的
    list_x = []
    for i in range(1,jishu+1):
        list_x.append(i)
    print("横坐标：",list_x)

    list_y = []
    for i in range(jishu):   #这里的jishu是自定义的，不是灵活的
        print("这是第 ",i+1," 次迭代")
        if start <= stop:
            start,stop = (int(start),int(stop))
        else:
            stop, start = (int(start), int(stop))
        #print(start,stop)

        list = []
        for i in range(length):
            #print(i)
            if i == 0:
                x = random.randint(start,stop)
                print("随机数是：" , x)
            j = random.randint(start,stop)
            list.append(j)
            #print(list)
            num_x = list.count(x)
        print("随机数出现的次数：",num_x)
        show_rate = num_x/length
        print("出现率：",show_rate)

        list_y.append(show_rate)
        print("----------------------------------")
    print("纵坐标：",list_y)

    plt.plot(list_x, list_y, label='NM')
    # plt.plot(x2, y2, label='Second Line')
    plt.xlabel('The number of iteration')  # 横坐标标题
    plt.ylabel('The rate of appearance')  # 纵坐标标题
    plt.title('The Distribution of  one number \n in random list',loc="center")   #图像标题
    # plt.title('Interesting Graph\nCheck it out')
    plt.legend()  # 显示Fisrt Line和Second Line（label）的设置
    plt.savefig('C:/Users/zhengyong/Desktop/1.png')
    plt.show()

random_list(1,10,10000)
