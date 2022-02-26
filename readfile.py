# f=open("record.txt","r")
# for x in f:
#     print(x,end="")

f=open("record.txt","a") #read in the file
f=open('record.txt','w') #this mehod overite the written content in the file
f.write("Content written in file.")
f.close()
f.open("record.txt","r")
print(f.read())