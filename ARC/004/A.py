import itertools

N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

n = [i for i in range(N)]
ans = 0
for i in itertools.combinations(n, 2):
    tmp = ((x[i[0]] - x[i[1]]) ** 2 + (y[i[0]] - y[i[1]]) ** 2) ** 0.5
    if tmp > ans:
        ans = tmp

print(ans)
