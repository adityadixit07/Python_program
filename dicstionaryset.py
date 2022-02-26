x=int(input("enter the no of boxes:"))
Box=dict()
for i in range(x):
  y=input("enter the name of box:")
  box=[]
  z=input("enter the surface area of the box:")
  box.append("surface area="+z)
  a=input("enter the volume of the box:")
  box.append("volume:"+a)
  Box[y]=box
print(box)