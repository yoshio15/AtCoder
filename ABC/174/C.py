k = int(input())
x = 7 % k
s = set()
i = 1
while x not in s:
    if x == 0:
        print(i)
        exit(0)
    s.add(x)
    x = (x * 10 + 7) % k
    i += 1
print(-1)
