n, k = map(int, input().split())
vil = dict()
for i in range(n):
    a, b = map(int, input().split())
    if a in vil:
        vil[a] += b
    else:
        vil[a] = b
vil = sorted(vil.items())
now = 0
for i in range(len(vil)):
    if k + now < vil[i][0]:
        break
    else:
        k = k - (vil[i][0] - now)
        k += vil[i][1]
        now = vil[i][0]

print(k + now)
