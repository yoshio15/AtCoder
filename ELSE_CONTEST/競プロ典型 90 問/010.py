# input
n = int(input())
cp = [map(int, input().split()) for _ in range(n)]
c, p = [list(i) for i in zip(*cp)]
q = int(input())
lr = [map(int, input().split()) for _ in range(q)]
l, r = [list(i) for i in zip(*lr)]

# 累積和の算出
cum_sum_one = [0] * (n + 1)  # クラス1の累積和
cum_sum_two = [0] * (n + 1)  # クラス2の累積和
for i in range(n):
    if c[i] == 1:
        cum_sum_one[i + 1] = cum_sum_one[i] + p[i]
        cum_sum_two[i + 1] = cum_sum_two[i]
    else:
        cum_sum_one[i + 1] = cum_sum_one[i]
        cum_sum_two[i + 1] = cum_sum_two[i] + p[i]

# print("クラス1の累積和：{}".format(cum_sum_one))
# print("クラス2の累積和：{}".format(cum_sum_two))

for i in range(q):
    ans_one = cum_sum_one[r[i]] - cum_sum_one[l[i] - 1]
    ans_two = cum_sum_two[r[i]] - cum_sum_two[l[i] - 1]
    print("{} {}".format(ans_one, ans_two))
