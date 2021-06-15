n = int(input())
a = set()
b = set()
for _ in range(n):
    s = input()
    if s[0] != "!":
        a.add(s)
    else:
        b.add(s[1:len(s)])
ans = "satisfiable"
for x in a:
    if x in b:
        ans = x
        break
print(ans)
