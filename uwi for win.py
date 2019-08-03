import random
import datetime
import matplotlib.pyplot as plt

starttime = datetime.datetime.now()
lenth_list = 10
iterations = 100

A,L = 0,0
x = []
winrate = []
for n in range(1,101):
    x.append(n*iterations)
    for i in range(0,n*iterations):

        list = []
        for i in range(0, lenth_list):
            n = random.randint(0, lenth_list)
            list.append(n)
        # print(list)

        Alex = []
        Lee = []

        while len(list) > 0:
            min_num = 0
            max_num = len(list)-1
            #print(max_num)
            if list[min_num] > list[max_num]:
                #print("Alex")
                Alex.append(list[min_num])
                list.remove(list[min_num])
            else:
                Alex.append(list[max_num])
                list.remove(list[max_num])

            #print("changdu",len(list))

            if list[min_num] > list[max_num-1]:
                Lee.append(list[min_num-1])
                list.remove(list[min_num-1])
                #print("Lee")
            else:
                Lee.append(list[max_num-1])
                list.remove(list[max_num-1])
        if sum(Alex) > sum(Lee):
            A = A + 1
        else:
            L = L + 1
        print(sum(Alex),sum(Lee))
    #print("The win-rate of second man:",L/(A+L)*100,"%")
    winrate.append(L/(A+L)*100)
print(x)
print(winrate)
print(len(winrate))
endtime = datetime.datetime.now()
print (endtime - starttime)

plt.plot(x, winrate, label='First choose first win')
#plt.plot(x2, y2, label='Second Line')
plt.xlabel('Iterations')  #横坐标标题
plt.ylabel('Winrate for second man')  #纵坐标标题
#plt.title('Interesting Graph\nCheck it out',loc="right")   #图像标题
#plt.title('Interesting Graph\nCheck it out')
plt.legend()    #显示Fisrt Line和Second Line（label）的设置
plt.savefig('C:/Users/zhengyong/Desktop/1.png')
plt.show()