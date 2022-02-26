class employee:
    company="microsoft"
    def f1(self):
        print("the company name is ",self.company)
class manager(employee):
    post="manager"
    salary=676566
    def f2(self):
        print("the salary is",self.salary,"and the post is",self.post)
m=manager()
m.f1()
m.f2()
f=open("storerecord.txt",'a')
data1=str("post",m.f2())
f.write(data1)

