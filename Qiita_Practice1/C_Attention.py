# [検証用]
# import time
#
# N = 100000
# S = ""
# for i in range(N):
#     if i % 2 == 0:
#         S += "W"
#     else:
#         S += "E"
# start = time.time()

N = int(input())
S = input()
ans = N

# 【パターンA】
# N = 100000の時、実行速度:8142.369747161865[ms]
# for i in range(N):
#     cnt = S[:i].count("W") + S[i + 1:].count("E")
#     if ans > cnt:
#         ans = cnt

# 【パターンB（累積和）】
# N = 100000の時、実行速度:107.47003555297852[ms]
cum_sum_w = [0] * (N + 1)
cum_sum_e = [0] * (N + 1)
for i in range(N):
    if S[i] == "W":
        cum_sum_w[i + 1] = cum_sum_w[i] + 1
        cum_sum_e[i + 1] = cum_sum_e[i]
    else:
        cum_sum_w[i + 1] = cum_sum_w[i]
        cum_sum_e[i + 1] = cum_sum_e[i] + 1

for i in range(N):
    cnt = cum_sum_w[i] + cum_sum_e[N] - cum_sum_e[i + 1]
    if ans > cnt:
        ans = cnt

print(ans)

# end = time.time()
# _time = (end - start) * 1000
# print("実行速度:{0}[ms]".format(_time))
