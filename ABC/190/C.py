n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
ab_cnt = {}
for el in ab:
    if el[0] in ab_cnt:
        ab_cnt[el[0]] += 1
    else:
        ab_cnt[el[0]] = 1
    if el[1] in ab_cnt:
        ab_cnt[el[1]] += 1
    else:
        ab_cnt[el[1]] = 1
ab_cnt_sorted = sorted(ab_cnt.items(), key=lambda x: x[1], reverse=True)
tmp = {}
for el in ab_cnt_sorted:
    tmp[el[0]] = False
k = int(input())
cd = [list(map(int, input().split())) for _ in range(k)]
ans_list = []
for el in cd:
    for k, v in tmp.items():
        if el[0] == k and not v:
            ans_list.append(el[0])
            tmp[k] = True
            break
        elif el[1] == k and not v:
            ans_list.append(el[1])
            tmp[k] = True
            break
ans = 0
for el in ab:
    if el[0] in ans_list and el[1] in ans_list:
        ans += 1
print(ans)
