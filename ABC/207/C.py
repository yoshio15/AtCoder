n = int(input())
tlr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    tar_t = tlr[i][0]
    tar_l = tlr[i][1]
    tar_r = tlr[i][2]
    for j in range(i + 1, n):
        t = tlr[j][0]
        l = tlr[j][1]
        r = tlr[j][2]
        if r >= tar_l and tar_r >= l:
            if r == tar_l and tar_r != l:
                if (tar_t == 1 or tar_t == 2) and (t == 1 or t == 3):
                    ans += 1
            elif r != tar_l and tar_r == l:
                if (tar_t == 1 or tar_t == 3) and (t == 1 or t == 2):
                    ans += 1
            else:
                ans += 1
print(ans)
