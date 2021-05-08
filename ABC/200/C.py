import collections

# Input
N = int(input())
a = list(map(int, input().split()))


# Calculate "nCr"
def cmb(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


ans = 0
cnt = collections.Counter(list(map(lambda x: x % 200, a)))

for el in cnt.values():
    if el > 1:
        ans += cmb(el, 2)

print(ans)
