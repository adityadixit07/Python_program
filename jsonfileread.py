import json
x=open('newfile.json','r')
y=json.load(x)
print(y)
z={
    "newname":["aditya","renuka patel","Divyanjali","subhangi Mishra"]
}

print(json.dumps(z))