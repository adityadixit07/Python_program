import matplotlib.pyplot as pt
# print(matplotlib.__version__)
import numpy as np
x=np.array([0,2,3,4,5])
y=np.array([0,2,0,2,0])
# pt.plot(xp,yp,'o') to draw the start and end points
#pt.plot(xp,yp,'o:r') #to show dotted lines
# pt.pie(x) draw pie chart
pt.plot(x,y)
# pt.xlabel("x-axis")
# pt.ylabel("y-axis")
pt.show()