n = int(input())

MAX = 1000
graph = [[0] * MAX for _ in range(MAX)]

for i in range(n):
    lx, ly, rx, ry = map(int, input().split())
    for j in range(rx - lx):
        for k in range(ry - ly):
            graph[lx + j][ly + k] += 1

# for row in graph:
#     print(row)

ans_list = []
for i in range(n):
    cnt = 0
    for j in range(MAX):
        for k in range(MAX):
            if graph[j][k] == i + 1:
                cnt += 1
    ans_list.append(cnt)

for ans in ans_list:
    print(ans)
