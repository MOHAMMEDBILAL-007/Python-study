# print("hello","heha","kjsdbhcidsj",sep=" .. ")
# c = 1+2j
# print(type(c))
# st = """dowhat
# everyou
# wanti
# dontcare"""
# print(st)
# # for i in st:
# #     print(i)
# st ="hsdgcuuhsdhsjaihdoaisdiahsdhsdakjkjdhajska"
# print(st[3])
# print(len(st))
# print(st[:])

# import time
# print(time.time())
# print(time.ctime())
# print(time.localtime())
# print(time.gmtime())
# hour = time.strftime("%H")
# minute = time.strftime("%M")
# seconds= time.strftime("%S")
# hour = int(hour)%12
# print(hour,":",int(minute),":",int(seconds))


# import time
# sttime = time.time()
# x = 0
# for i in range(1000):
#     x+=i
# print(x)
# print(time.time()-sttime)
# i = 10
# while True:
#     print(i)
#     if i >5:
#         break

import os

os.chdir("d:\learning\Python-study\self learning")

with open("manage 49.txt") as f:
    while True:
        if not f.readline():
            break
        print(f.readline())
    
        