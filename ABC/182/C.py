n = input()
ans = -1
for i in range(2 ** len(n)):
    tl = []
    for j in range(len(n)):
        if (i >> j) & 1:
            tl.append(int(n[j]))
    s_tl = sum(tl)
    if s_tl != 0 and s_tl % 3 == 0:
        tmp = len(n) - len(tl)
        if ans == -1:
            ans = tmp
        else:
            ans = min(ans, tmp)
print(ans)
