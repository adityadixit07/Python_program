def pattern(n):
    # rows
    for row in range(n): 
        # columns
        for col in range(n): 
            if ((row == 0 and (col != 0 and col != n-1)) or               
                (row == n - 1 and (col != 0 and col != n-1)) or                
                ((col == 0 and (row != 0 and row != n-1)) or                 
                 (col == n-1 and row != n-1 and row >= (n/2)-1)) or                
                (row == (n/2)-1 and ((n/2)-1 <= col < n-1))
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
# driver code
n = int(input("Enter the size you want: \t"))
if n < 8:
    print("Enter a size greater than 8")
else:
    pattern(n)