class employee:
    companyname="Micrsoft"
    def f1(self):
        print("your company is ",self.companyname)
class manager(employee):
    salary=4545
    post="manager"
    def f1(self):
        print("company name is ",self.companyname,"and his salary is",self.salary,"and his post is",self.post)
class worker(employee):
    workarea="noida"
    salary=12200
    post="Worker"
    def f1(self):
        print("The post is",self.post,"and the work area is",self.workarea,"and his salary is",self.salary)
m=manager()
m.f1()
w=worker()
w.f1()