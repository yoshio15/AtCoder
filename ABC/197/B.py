H, W, X, Y = map(int, input().split())
S = [""] * H
for i in range(H):
    S[i] = input()

block = "#"
no_block = "."

ans = 0
if S[X - 1][Y - 1] == no_block:
    ans += 1

# 上方向
for i in range(H):
    if X - i - 2 < 0:
        break
    if S[X - i - 2][Y - 1] == block:
        break
    ans += 1

# 下方向
for i in range(H):
    if X + i > H - 1:
        break
    if S[X + i][Y - 1] == block:
        break
    ans += 1

# 左方向
for i in range(W):
    if Y - i - 2 < 0:
        break
    if S[X - 1][Y - i - 2] == block:
        break
    ans += 1

# 右方向
for i in range(W):
    if Y + i > W - 1:
        break
    if S[X - 1][Y + i] == block:
        break
    ans += 1

print(ans)
