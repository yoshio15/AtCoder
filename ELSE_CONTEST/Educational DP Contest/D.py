N, W = map(int, input().split())
wv = [map(int, input().split()) for _ in range(N)]
w, v = [list(i) for i in zip(*wv)]

# dp[i] := i-1 番目までの品物から重さが W を超えないように選んだときの、価値の総和の最大値
# dp[i][sum_w] := i-1 番目までの品物から重さが sum_w を超えないように選んだときの、価値の総和の最大値
dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(N + 1):
    if i == 0:
        continue
    for j in range(W + 1):
        if j == 0:  # 重さが0の時は何も選べないためスキップ
            continue
        tmp = 0
        if j >= w[i - 1]:  # j(sum_w) が i-1 番目の品物より大きい場合
            tmp = dp[i - 1][j - w[i - 1]] + v[i - 1]
            if tmp > dp[i - 1][j]:
                dp[i][j] = tmp
            else:
                dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j]

# print(dp)
print(dp[N][W])
