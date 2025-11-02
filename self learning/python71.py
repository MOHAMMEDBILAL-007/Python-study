x =[1,2,3,4,4]
print(dir(x))
print(x.__add__)

class mixt:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
e = mixt("luffy",20)
print(e.__dict__)

help(int)