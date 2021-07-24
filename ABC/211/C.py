CHOKUDAI = 'chokudai'
s = input()
mod = 10 ** 9 + 7
dp = [[0] * (len(s) + 1) for _ in range(len(CHOKUDAI))]
for i in range(len(CHOKUDAI)):
    for j in range(len(s) + 1):
        if j == 0 or j > len(s):
            continue
        if i == 0:
            if s[j - 1] == CHOKUDAI[i]:
                dp[i][j] = dp[i][j - 1] + 1
            else:
                dp[i][j] = dp[i][j - 1]
        else:
            if s[j - 1] == CHOKUDAI[i]:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]
# for el in dp:
#     print(el)
print(dp[len(CHOKUDAI) - 1][len(s)] % mod)
