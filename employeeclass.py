
class employee:
    name=str(input("enter the name:_"))
    income=int(input("enter the income:_"))
    def f1(self,n,i):
        self.name=n
        self.income=i
       
        print("the name is"+self.name)
        print("the employee income is"+self.income)
    def f1(self):
        print("the employee name is",self.name,"and the salary is",self.income)
    
e1=employee()
print("The employee record is:-")
e1.f1()