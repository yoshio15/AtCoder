n = int(input())
ng = set()
x = 2
while x ** 2 <= n:
    y = 2
    while x ** y <= n:
        ng.add(x ** y)
        y += 1
    x += 1
print(n - len(ng))
