s = input()

if len(s) % 2 == 0:
    s = s[:-2]
else:
    s = s[:-1]

while s[:len(s)//2] != s[len(s)//2:]:
    s = s[:-2]

print(len(s))

