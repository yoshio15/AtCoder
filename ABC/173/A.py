n = int(input())
ans = 0
for i in range(10):
    tmp = (i + 1) * 1000
    if tmp >= n:
        ans = tmp - n
        break
print(ans)
