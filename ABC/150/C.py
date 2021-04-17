import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

origin = [i + 1 for i in range(N)]
a = 0
b = 0
for i, per in enumerate(itertools.permutations(origin)):
    if per == P:
        a = i + 1
    if per == Q:
        b = i + 1

print(abs(a - b))
