h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]
cnt = 0
for i in range(2 ** h):
    print("-----------------------------")
    rows = []
    for j in range(h):
        if (i >> j) & 1:
            rows.append(j + 1)
    for j in range(2 ** w):
        cols = []
        for k in range(w):
            if (j >> k) & 1:
                cols.append(k + 1)
        print("-----")
        print("選択行: {}".format(rows))
        print("選択列: {}".format(cols))
        # TODO: 選択行・列以外の黒の数をカウントする
        # 黒の数が K と等しかった場合、カウントアップしていく
print(cnt)
