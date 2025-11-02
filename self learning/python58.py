class person:
    name = "isagi"
    occupation = "u20 striker"
    networth = 190000000
    def worldcup(self):
        print(f"player name: {self.name} \noccupation : {self.occupation}")
player1 = person()
player1.name = "ichigo"
player1.occupation = "soul reaper"
player1.worldcup()
# in the above class i have created default values for the variable 
# which there is no need to do because a class is a tamplet that should have no value
# this is where constructors come to use

class user:
    def __init__(self):# this is a constructor it constructs the properties of the object every time the object is created
        print("hey iam a user")
        # this is a default constructor because it doesent take any argument other than self
user1 = user()#here the __init__ is called the moment this object is created

# with this constructor we can initialize the values as arguments while creating the object

class player():
    def __init__(self,name, occupation,networth):# this method helps the class take the values as arguments while creating the object of the class
        self.name = name
        self.occupation = occupation
        self.networth = networth
    def display(self):
        print(f"name: {self.name}\noccupation: {self.occupation}\nnetworth: {self.networth}")


player1 = player("naruto","hokage",1000000)# here constructor assigned the values
player1.display()

player2 = player("boruto","usless trash",10000)
player2.display()