h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
black = "#"
ans = []
for el in a:
    if black in el:
        ans.append(el)
ver = []
for i in range(w):
    tmp = []
    for j in range(len(ans)):
        tmp.append(ans[j][i])
    ver.append(tmp)
ver2 = []
for el in ver:
    if black in el:
        ver2.append(el)
ans = [[""] * len(ver2) for _ in range(len(ver2[0]))]
for i in range(len(ver2)):
    for j in range(len(ver2[i])):
        ans[j][i] = ver2[i][j]
for el in ans:
    print("".join(el))
