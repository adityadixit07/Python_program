from traceback import print_tb


def f(x):
    print(x[0])
    x[2]=90
y=[43,56,234,67,5324,423]
f(y)
print(y)