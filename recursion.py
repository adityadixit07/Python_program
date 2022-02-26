def f1(x):
    if x<0:
        return 1
    else:
        return x*f1(x-1)
x=3
print(f1(x))
    