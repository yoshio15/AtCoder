import itertools
n = int(input())
abcde = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
for i in itertools.combinations(abcde, 3):
    a, b, c, d, e = [list(i) for i in zip(*i)]
    team_score = [max(a), max(b), max(c), max(d), max(e)]
    total_score = min(team_score)
    if total_score > ans:
        ans = total_score

print(ans)
