import csv
from matplotlib import pyplot as plt

try:
    f=open('csbfile.csv','r')
    file=csv.DictReader(f) #dic reader read in column wise.
    name=[]
    rollno=[]
    age=[]
    for i in file:
        name.append(i['Name'])
        age.append(i['Age'])
        rollno.append(i['Roll No.'])
    print(name)    
    print(rollno)    
    print(age)    
    plt.plot(rollno,age)
    plt.show()
except :
    pass