num=int(input("enter the number"))
for x in range(1,11):
  table=num*x
  print("{a}*{b}={c}".format(a=num,b=x,c=table))