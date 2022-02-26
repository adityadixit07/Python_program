N=3
def transpose(a,b):
    for i in range(N):
       for j in range(N):
           b[i][j]=a[j][i]
    
a=[[1,2,3],[2,3,45],[45,67,87]]
b=a[:][:]
print(a)
transpose(a,b)
print("the result of matrix ix:")
for i in range (N):
     for j in range(N):
       print(b[i][j]," ",end='')
     print()