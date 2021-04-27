# https://note.com/taraba_kanico/n/n8aca58bcd303
# import itertools
#
# N = int(input())
# A = list(map(int, input().split()))
#
# ans = 0
# for i in itertools.combinations(A, 2):
#     ans += (i[0] - i[1]) ** 2
#
# print(ans)

n = int(input())
a = [i for i in input().split()]
keys = [i for i in range(-200, 201)]
values = [0] * 401
cnt = dict(zip(keys, values))
for i in range(-200, 201):
    cnt[i] = a.count(str(i))
ans = 0
for i in range(-200, 200):
    for j in range(i + 1, 201):
        # print("---i={}, j={}---".format(i, j))
        ans += cnt[i] * cnt[j] * (i - j) ** 2

print(ans)
