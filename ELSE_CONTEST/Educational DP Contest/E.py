N, W = map(int, input().split())
wv = [map(int, input().split()) for _ in range(N)]
w, v = [list(i) for i in zip(*wv)]

# dp[i][sum_v] := i-1 番目までの品物から価値が sum_v となるように選んだときの、重さの総和の最小値
max_v = 1001
INF = 10 ** 9 + 1
dp = [[INF] * max_v for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N + 1):
    if i == 0:
        continue
    for j in range(max_v):
        if j == 0:
            continue
        if j >= v[i - 1]:
            tmp = dp[i - 1][j - v[i - 1]] + w[i - 1]
            if dp[i - 1][j] > tmp:
                dp[i][j] = tmp
            else:
                dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j]

ans = INF
print(dp[N])
for j in range(max_v):
    if dp[N][j] <= W:
        print(j)
        ans = j

# print(dp)
print(ans)
