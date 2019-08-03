import random
list = []
for i in range(0,100):
    n = random.randint(0,100)
    list.append(n)
print(list)
list.remove(list[0])
print(sum(list))