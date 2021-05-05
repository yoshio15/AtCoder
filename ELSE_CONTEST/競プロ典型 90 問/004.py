h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

row_total = [sum(i) for i in a]  # 各行の総和
col_total = [0] * w  # 各列の総和
for i in range(w):
    col_total[i] = sum([el[i] for el in a])

ans_list = [[""] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        ans_list[i][j] = str(row_total[i] + col_total[j] - a[i][j])

for i in range(h):
    print(" ".join(ans_list[i]))
