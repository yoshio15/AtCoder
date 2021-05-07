n = int(input())
a, b, c = map(int, input().split())

L = 9999

# aの枚数: i
# bの枚数: j
# cの枚数: (n - a * i - b * j)/ c
ans = 10000
for i in range(L + 1):
    for j in range(L - i):
        rest = n - a * i - b * j
        if rest < 0:
            break
        if rest % c == 0:
            k = rest // c
            tmp = i + j + k
            if tmp < ans:
                ans = tmp

print(ans)
