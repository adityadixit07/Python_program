while True:
    try:
        a = int(input("Enter a number= "))
        print("this is number")
        break
    except ValueError:
        print("This is not a number.")
        print()