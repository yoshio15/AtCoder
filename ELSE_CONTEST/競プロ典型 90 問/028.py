n = int(input())

MAX = 1000
graph = [[0] * 1009 for _ in range(1009)]

# 二次元いもす法
for i in range(n):
    lx, ly, rx, ry = map(int, input().split())
    graph[lx][ly] += 1  # 左下
    graph[lx][ry] -= 1  # 左上
    graph[rx][ly] -= 1  # 右下
    graph[rx][ry] += 1  # 右上

for x in range(MAX):
    for y in range(1, MAX):
        graph[x][y] += graph[x][y - 1]

for x in range(1, MAX):
    for y in range(MAX):
        graph[x][y] += graph[x - 1][y]

ans_list = [0] * n
for i in range(MAX):
    for j in range(MAX):
        if graph[i][j] >= 1:
            ans_list[graph[i][j] - 1] += 1

for ans in ans_list:
    print(ans)
