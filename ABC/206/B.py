n = int(input())
ans = 0
x = 0
i = 0
while True:
    i += 1
    x += i
    if x >= n:
        ans = i
        break
print(ans)
