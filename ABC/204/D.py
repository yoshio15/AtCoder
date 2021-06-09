n = int(input())
t = list(map(int, input().split()))
s = sum(t)

dp = [[False] * (s + 1) for _ in range(n + 1)]
dp[0][0] = True

for i in range(n):
    for j in range(s + 1):
        if dp[i][j]:
            dp[i + 1][j] = True
        if j - t[i] >= 0 and dp[i][j - t[i]]:
            dp[i + 1][j] = True

ans = 10 ** 10
for i in range(s + 1):
    if dp[n][i]:
        score = max(i, s - i)
        ans = min(ans, score)
print(ans)
