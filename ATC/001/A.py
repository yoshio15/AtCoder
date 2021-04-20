# A - 深さ優先探索
H, W = map(int, input().split())
S = [[""] * W for i in range(H)]
history = [[0] * W for i in range(H)]  # 探索済みの場合：1, 未探索の場合：2
start = "s"
goal = "g"
block = "#"
way = "."
sx = 0
sy = 0

for i in range(H):
    S[i] = list(input())
    if start in S[i]:
        sx = i
        sy = S[i].index(start)

history[sx][sy] = 1  # スタート地点は探索済み

# 探索候補をスタックに入れる
stack = []


# 探索可能なルートをスタックに入れる
def search_available_route(x, y):
    if x > 0:
        # 上方向
        if S[x - 1][y] != block and history[x - 1][y] == 0:
            stack.append((x - 1, y))
    if y > 0:
        # 左方向
        if S[x][y - 1] != block and history[x][y - 1] == 0:
            stack.append((x, y - 1))
    if y < W - 1:
        # 右方向
        if S[x][y + 1] != block and history[x][y + 1] == 0:
            stack.append((x, y + 1))
    if x < H - 1:
        # 下方向
        if S[x + 1][y] != block and history[x + 1][y] == 0:
            stack.append((x + 1, y))


search_available_route(sx, sy)
while len(stack) > 0:
    next_po = stack.pop()
    nx = next_po[0]
    ny = next_po[1]
    if S[nx][ny] == goal:
        print('Yes')
        exit(0)
    history[nx][ny] = 1
    search_available_route(nx, ny)

print('No')
