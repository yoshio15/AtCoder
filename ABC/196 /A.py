a, b = map(int, input().split())
c, d = map(int, input().split())
ans = a - c
if a - d > ans:
    ans = a - d
if b - c > ans:
    ans = b - c
if b - d > ans:
    ans = b - d
print(ans)
