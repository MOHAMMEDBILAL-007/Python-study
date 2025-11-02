class employee:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "this is str dunder method"
    
    def __repr__(self):
        return f"dunder_method(__repr__)"
    
    def __call__(self):
        print("present")

    def __len__(self):
        j= 0
        for i in self.name:
            j +=1
        return j
    
c = employee("shadow")
print(c.name)
print(len(c))
print(c)
print(str(c))
print(repr(c))
c()

