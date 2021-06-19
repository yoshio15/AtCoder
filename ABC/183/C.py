import itertools

n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
base = [i + 1 for i in range(n - 1)]
ans = 0

for el in itertools.permutations(base):
    tot = 0
    nw = 0
    for nx in el:
        tot += t[nw][nx]
        nw = nx
    tot += t[nw][0]
    if tot == k:
        ans += 1
print(ans)
