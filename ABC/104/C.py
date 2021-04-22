# 微妙に分からん
D, G = map(int, input().split())
pc = [map(int, input().split()) for _ in range(D)]
p, c = [list(i) for i in zip(*pc)]

print(p)
print(c)

ans = sum(p)
k = 1
for i in range(2 ** D):
    total = 0
    cnt = 0
    print("i: {}".format(i))
    for j in range(D):
        if (i >> j) & 1:
            # 全完
            cnt += p[k - 1]
            total += 100 * k * p[k - 1] + c[k - 1]
    print("パターン{}: {}".format(k, total))
    print("解いた数: {}問".format(cnt))
    if total > G:
        print("多すぎ")
        continue
    else:
        print("中途半端に計算して追加する")

    if i + 1 % 2 == 0:
        k += 1
