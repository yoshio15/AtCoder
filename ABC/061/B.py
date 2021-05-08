n, m = map(int, input().split())

w_cnt = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    w_cnt[a - 1] += 1
    w_cnt[b - 1] += 1

for el in w_cnt:
    print(int(el))
