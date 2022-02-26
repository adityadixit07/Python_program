class A:
      def f1(self):
        print('parent classs')
class B(A):
  def f1(self):
      super().f1()
      print("Inside child class")
b=B()
b.f1()
#b=A()
#b.f1()