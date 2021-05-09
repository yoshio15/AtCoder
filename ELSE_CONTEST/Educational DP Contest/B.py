n, k = map(int, input().split())
h = list(map(int, input().split()))

INF = 10 ** 9 + 1
dp = [INF] * n
dp[0] = 0

for i in range(n):
    for j in range(1, k + 1):
        if i + j > n - 1:
            break
        tmp = dp[i] + abs(h[i] - h[i + j])
        if dp[i + j] > tmp:
            dp[i + j] = tmp
        # min() 関数を使うと WA になるケースがある
        # dp[i + j] = min(dp[i + j], dp[i] + abs(h[i] - h[i + j]))

# print(dp)
print(dp[n - 1])
