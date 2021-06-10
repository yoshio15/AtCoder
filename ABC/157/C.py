n, m = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(m)]
ans = -1
for i in range(1000):
    i_str = str(i)
    if len(i_str) != n:
        continue
    is_ok = False
    if m == 0:
        ans = i
        break
    for j in range(m):
        s = sc[j][0]
        c = sc[j][1]
        if i_str[s - 1] != str(c):
            is_ok = False
            break
        else:
            is_ok = True
    if not is_ok:
        continue
    ans = i
    break
print(ans)
