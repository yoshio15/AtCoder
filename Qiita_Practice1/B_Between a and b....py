a, b, x = map(int, input().split())

ans = (b // x) - (a // x)
if a % x == 0:
    ans += 1

print(ans)
