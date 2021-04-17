import itertools
import statistics
import math

N = int(input())
xy = [list(map(int, input().split())) for l in range(N)]

dis_list = [0] * math.factorial(N)
for i, p_tuple in enumerate(itertools.permutations(xy)):
    dis = 0
    for k in range(len(p_tuple) - 1):
        x1 = p_tuple[k][0]
        x2 = p_tuple[k+1][0]
        y1 = p_tuple[k][1]
        y2 = p_tuple[k+1][1]
        dis += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    dis_list[i] = dis

print(statistics.mean(dis_list))
