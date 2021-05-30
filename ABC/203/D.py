import statistics

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 10 ** 9 + 1
for i in range(n - k + 1):
    for j in range(n - k + 1):
        ar = []
        for x in range(k):
            for y in range(k):
                ar.append(a[i + x][j + y])
        tmp = statistics.median_low(ar)
        if tmp < ans:
            ans = tmp

print(ans)
