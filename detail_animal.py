class animal:
    def input(self):
        self.name=input("enter the name of the animal:")
        self.color=input("enter the color of the animal:")
        self.breed=input("enter the breed of the animal:")
    def display(self):
        print(self.name,"color",self.color,"breed",self.breed)
a=animal()
a.input()
a.display()
