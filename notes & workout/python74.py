class parent:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    def area(self):
        return self.x * self.y

class child(parent):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return (3.14 *(self.radius*self.radius))# overriding parent class
rect = parent(3,4)
print(rect.area())

circle = child(9)
print(circle.area())


#lets go complex
class parent1:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    def area(self):
        return self.x * self.y
class child1(parent1):
    def __init__(self,radius):
        super().__init__(radius,radius)
        self.radius = radius
    def area(self):
        return (3.14 * (self.radius*self.radius))
circ= child(4)
print(circ.area())
