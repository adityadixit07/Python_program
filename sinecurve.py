from turtle import color
import matplotlib.pyplot as pt
import numpy as np
# import math
# x=np.array([0,np.pi/2,np.pi,(3*np.pi)/2,2*np.pi])
# y=np.array([0,1,0,-1,0])
x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.sin(x)
pt.axhline(y=0)
pt.xlabel("x-axis")
pt.ylabel("y-axis")
pt.plot(x,y,linestyle='dashed',color='r')
pt.show()