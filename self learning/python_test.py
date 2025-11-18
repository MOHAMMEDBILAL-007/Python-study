f = open("D:\learning\Python-study\self learning\manage 49.txt",'r')
for i in f.readlines():
    L1 = list(j for j in list(i.split(" ")) if j != "\n")
    print(L1)