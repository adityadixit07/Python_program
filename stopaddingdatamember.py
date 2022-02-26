try:
    class student:
        def record(self):
            self.age=int(input("enter your age.."))
            self.name=input("enter your name..")
        def display(self):
            # print(f"name is {self.name} and age is {self.age}.")
            print("name is {} and age is {}".format(self.name,self.age))
    s=student()
    s.record()
    s.display()
except:
    print("error")
