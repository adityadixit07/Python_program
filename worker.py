class worker:
    def work(self):
        self.name=input("enter the name>>")
        self.salary=int(input("enter the salary>>"))
    def display(self):
        print(f"wroker name is {self.name} and their work salary is {self.salary} rupees.")
w=worker()
w.work()
w.display()
        