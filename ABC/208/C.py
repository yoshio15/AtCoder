n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = k // n
base = 0
if k % n != 0:
    s_a = sorted(a)
    base = s_a[k % n - 1]
for ai in a:
    if ai <= base:
        print(ans + 1)
    else:
        print(ans)
