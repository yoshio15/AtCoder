a, b, c = map(int, input().split())
ans = 0
if a == b:
    ans = c
elif a == c:
    ans = b
elif b == c:
    ans = a
print(ans)
