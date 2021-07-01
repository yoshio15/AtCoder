n = int(input())
ans_list = []
ans = 0
for c in range(1, n):
    tar = n - c
    for a in range(1, tar + 1):
        if tar % a == 0:
            # tmp = [a, tar // a, c]
            # ans_list.append(tmp)
            ans += 1
# print(ans_list)
print(ans)
