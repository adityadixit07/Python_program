#Box class
class Box:
  def cuboid(self):
    self.l=int(input("enter the length:"))
    self.b=int(input("enter the breadth:"))
    self.h=int(input("enter the height:"))
  def cube(self):
    self.side=int(input("enter the side of the cube:"))
    
  def display(self):
    print("the volume of cuboid is",self.l*self.b*self.h)
    print("the voulume of cube is ",self.side*self.side*self.side)
b=Box()
b.cuboid()
b.cube()
b.display()