import collections

n = int(input())
graph = [[] for _ in range(n)]  # 各頂点がどこの頂点と隣接しているかを保持

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b)
    graph[b - 1].append(a)


def get_dist(start):
    dist = [-1] * (n + 1)  # 任意の頂点から頂点iへの距離
    dist[0] = 0
    dist[start] = 0
    queue = collections.deque()
    queue.append(start)
    while len(queue) > 0:
        now_c = queue.popleft()
        for next_c in graph[now_c - 1]:
            if dist[next_c] != -1:
                continue
            dist[next_c] = dist[now_c] + 1
            queue.append(next_c)

    return dist


# 1. 木構造の直径を求める
#  1-1. 任意の点 u からの最大距離となる点 A を求める
dist_l = get_dist(1)
max_i = dist_l.index(max(dist_l))
#  1-2. A から最大距離となる点 B を求める(点A-B間の距離が木構造の直径)
dist_l = get_dist(max_i)

# 2. 直径 + 1 が解答
print(max(dist_l) + 1)
