n = int(input())
abc = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0, 0, 0] for _ in range(n + 1)]

for i in range(n):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            tmp = dp[i][j] + abc[i][k]
            if tmp > dp[i + 1][k]:
                dp[i + 1][k] = tmp

# for i in range(n + 1):
#     print("{}日目: {}".format(i, dp[i]))

print(max(dp[n]))
