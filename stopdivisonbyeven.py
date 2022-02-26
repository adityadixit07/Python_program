x=int(input("Enter the first number>>"))
y=int(input("Enter the second number>>"))
try:
    if(y%2!=0):
        print(x/y)
    else:
        raise Exception("Don't divide by even numbers.")
except:
    print("Unwanted conditon occured!")
    