n = int(input())
a = list(map(int, input().split()))
a.sort()
cum_sum = [0] * (n + 1)
for i in range(n):
    cum_sum[i + 1] = a[i] + cum_sum[i]

ans = 0
for i in range(n):
    ans += a[i] * i
    ans -= cum_sum[i]

print(ans)
