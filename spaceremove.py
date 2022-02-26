s = input()
n = ''
for i in range(0, len(s)):
    if s[i] != ' ':
        n += s[i]
print(n)