n = int(input())
a = list(map(int, input().split()))
step = 0
bef = a[0]
for i in range(1, len(a)):
    if bef > a[i]:
        step += bef - a[i]
    bef = max(bef, a[i])
print(step)
