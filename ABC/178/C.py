import math


def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


N = int(input())
ans = 0
mod = 10 ** 9 + 7
if N > 1:
    ans = comb(N, 2) * 2 * (10 ** (N - 2))

print(ans % mod)
