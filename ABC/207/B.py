a, b, c, d = map(int, input().split())
ans = -1
if c * d > b:
    i = 1
    while True:
        if c * d * i >= a + b * i:
            ans = i
            break
        i += 1
print(ans)
