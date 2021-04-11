R, X, Y = map(int, input().split())

ans = 0
distance = (X ** 2 + Y ** 2) ** 0.5

if distance < R:
    ans = 2
else:
    if distance % R == 0:
        ans = int(distance / R)
    else:
        ans = int(distance / R + 1)

print(ans)
