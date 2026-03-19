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

# import os

# os.chdir("d:\learning\Python-study\self learning")

# with open("manage 49.txt") as f:
#     while True:
#         if not f.readline():
#             break
#         print(f.readline())
    
# def fact(x):
#     return x if x<=1 else x*fact(x-1)
# print(fact(5))
# def mfact(x):
#     f = 1
#     for i in range(1,x+1):
#         f*=i
#     return f
# print(mfact(5))

# def fib(x):
#     if x == 0 :
#         return 0
#     elif x == 1 :
#         return 1
#     else :
#         return fib(x-1)+fib(x-2)
# i = int(input("Enter till where you want to print fibonacci series : "))
# for i in range(i+1):
#     print(fib(i),end = " ")

# class coco():
#     def __init__(self,name,age):
#         self._name =name
#         self.__age = age
#     def getter(self):
#         return self._name,self.__age
# s = coco("bilal",19)
# print(*s.getter())

# class cat:
#     def __init__(self):
#         self._name = None
#         self._age = None
#     @property
#     def details(self):
#         return self._name,self._age
    
#     @details.setter
#     def details(self,det):
#         name,age = det
#         self._name = name
#         self._age = age
# s = cat()
# s.details = ("bilal",20)
# print(*s.details)
# s.name = "b"
# print(*s.details)
# print(not None)