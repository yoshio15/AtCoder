n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    num = a[i]
    for j in range(i, n):
        num = min(num, a[j])
        ans = max(ans, num * (j + 1 - i))
print(ans)
