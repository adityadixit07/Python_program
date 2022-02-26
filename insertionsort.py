def insertionSort(n):   
    for i in range(1, len(n)):
        key = n[i]
        j=i-1
        while j >=0 and key < n[j] :
                n[j+1] = n[j]
                j -= 1
        n[j+1] = key
n= [12, 11, 13, 5, 6]
insertionSort(n)
print ("Sorted array is:")
for i in range(len(n)):
    print ("%d" %n[i])
         
