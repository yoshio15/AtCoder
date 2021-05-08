n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0
ans = "No"
for i in range(n):
    dif = abs(a[i] - b[i])
    cnt += dif

if cnt <= k:
    if (k - cnt) % 2 == 0:
        ans = "Yes"

print(ans)
