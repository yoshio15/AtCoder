n, x, t = map(int, input().split())
ans = n // x
if n % x != 0:
    ans += 1
print(ans * t)
