n = int(input())
h = list(map(int, input().split()))

INF = 10 ** 4 + 1
dp = [INF] * n
dp[0] = 0


for i in range(n):
    if i == 0:
        continue
    if i == 1:
        dp[i] = abs(h[i] - h[i - 1])
    else:
        dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2]))

# print(dp)
print(dp[n - 1])
