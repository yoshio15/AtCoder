n, a, x, y = map(int, input().split())
ans = 0
if n <= a:
    ans = x * n
else:
    ans = x * a + y * (n - a)
print(ans)
