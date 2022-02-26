from audioop import add


def findLen(str):
    counter = 0    
    for i in str:
        counter += 1
    return counter
  
  
str = "Aditya"
if str.len>4:
    add(str("his"))
    
print(findLen(str))