n = int(input())
a = list(map(int, input().split()))
l = a[0:2 ** (n - 1)]
r = a[2 ** (n - 1):2 ** n]
ai = min(max(l), max(r))
print(a.index(ai) + 1)
