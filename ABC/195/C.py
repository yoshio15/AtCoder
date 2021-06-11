n = int(input())
ans = 0
if n >= 1000:
    com = 1000
    while n - com + 1 > 0:
        ans += n - com + 1
        com *= 1000
print(ans)
