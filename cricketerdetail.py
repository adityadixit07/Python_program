class cricketer:
    def input(self):
        self.name=input("enter the name:")
        self.wickets=input("enter the wickets taken by the cricketer:")
        self.age=input("enter the  age of the Cricketer:")
    def display(self):
           print("the name of the player is",self.name,"and wickets taken by the player is",self.wickets,"and his age is",self.age,)
ct=cricketer()

a="yes"
while a=="yes":
    ct.input()
    ct.display()
    x=input("would you like to enter the more data.")