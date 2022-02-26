# from distutils.log import error
import os
# f=open("asd.txt","r")
# f.write("Future not decided.")
# f.write("hello")
# f=open('ad.txt','x')  x>>mode used to create bew file.
try:
    if os.path.exists('C:/Users/ADITYA/Desktop/pythonsem4/file'):
        print("Directory exists already.")
    else:
        d='file'
        parent_dir='C:/Users/ADITYA/Desktop/pythonsem4'
        file_name='newfile.txt'
        path=os.path.join(parent_dir,d)
        os.mkdir(path)
        file_path=os.path.join(path,file_name)
        f=open(file_path,"w")
        f.write("new file created successfully.")
        x=open(file_path,"r")
        print(x.read())
except:
    print('error')