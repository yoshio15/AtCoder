H, W = map(int, input().split())
S = []
black = "#"
white = "."
for i in range(H):
    S.append(list(input()))

ans = "Yes"
for i in range(H):
    for j in range(W):
        if S[i][j] == white:
            continue
        elif S[i][j] == black:
            for k in range(4):
                if not (i == 0) and k == 0:
                    if S[i - 1][j] == black:
                        break
                if not (j == 0) and k == 1:
                    if S[i][j - 1] == black:
                        break
                if not (j == W - 1) and k == 2:
                    if S[i][j + 1] == black:
                        break
                if not (i == H - 1) and k == 3:
                    if S[i + 1][j] == black:
                        break
                if k == 3:
                    ans = 'No'
                    print(ans)
                    exit(0)

print(ans)
