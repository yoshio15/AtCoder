import collections

n = int(input())
a = list(map(int, input().split()))
d = collections.Counter(a)
m = 0
for v in d.values():
    if v > 1:
        m += sum(list(range(1, v)))
x = sum(list(range(1, n)))
print(x - m)
