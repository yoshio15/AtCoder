N = int(input())
l = list(map(int, input().split()))

ans = 0
size = len(l)
for n in range(size):
    if (n + 1) % 2 == 0:
        ans -= max(l)
        l.remove(max(l))
    else:
        ans += max(l)
        l.remove(max(l))

print(ans)
