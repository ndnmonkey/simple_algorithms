def charu(list):
    num = len(list)
    for i in range(1,num):
        for j in range(0,i):
            print("i=",i,"j=",j,"      list[i]=",list[i],"list[j]=",list[j])
            if list[i] < list[j]:
                temp = list[i]
                list.remove(list[i])
                list.insert(j,temp)
                print(list)
                break
list = [3,44,39,5,47,15,36,26,27,2,46,4,19,50,48]  #13个数
charu(list)
