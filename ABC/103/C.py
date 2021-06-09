import math
import functools

n = int(input())
a = list(map(int, input().split()))


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm(*numbers):
    return functools.reduce(lcm_base, numbers, 1)


m = lcm(*a) - 1
ans = 0
for i in range(n):
    ans += m % a[i]
print(ans)
