s = input()
n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
l = ''
for i in range(0, len(s)):
    if s[i] not in n:
        l += s[i]
print(l)