class objects:
   count=0
   def __init__(self) :
        objects.count+=1
ob1=objects()
ob2=objects()
obj3=objects()
print("total objects created:",objects.count)