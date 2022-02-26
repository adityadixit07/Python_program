class A:
      def f1(self):
       print("parent class")
class B(A):
  def f1(self):
    super().f1()
    print("child class")
b=B()
b.f1()