n = int(input())
a = list(map(int, input().split()))

ans = 0
line = 0
for i in range(n):
    line += a[i] ** 2
ans = (sum(a) ** 2 - line) // 2

print(ans % (10 ** 9 + 7))

