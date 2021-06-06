x, y = map(int, input().split())
ans = 0
if x == y:
    ans = x
else:
    a = [0, 1, 2]
    a.remove(x)
    a.remove(y)
    ans = a[0]
print(ans)
