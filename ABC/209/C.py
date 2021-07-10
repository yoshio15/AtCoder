n = int(input())
c = list(map(int, input().split()))
mod = 10 ** 9 + 7
ans = 1
# c.sort()
c = sorted(c)
for i in range(n):
    ans *= c[i] - i
    if ans <= 0:
        ans = 0
        break
print(ans % mod)
