s = list(input())
ans = 0
r_cnt = 0
b_cnt = 0
for el in s:
    if el == "0":
        r_cnt += 1
    else:
        b_cnt += 1
ans = min(r_cnt, b_cnt) * 2
print(ans)
