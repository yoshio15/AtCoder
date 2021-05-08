a, b, c = map(int, input().split())


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


r = gcd(a, gcd(b, c))

print((a // r - 1) + (b // r - 1) + (c // r - 1))
