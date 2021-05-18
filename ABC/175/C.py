x, k, d = map(int, input().split())
ans = 0
if k * d <= abs(x):
    ans = abs(abs(x) - k * d)
else:
    rest = k - x // d
    ans = abs(abs(x) - abs(((x // d) + (rest % 2)) * d))
print(ans)
