c = [input().split() for _ in range(4)]
c.reverse()
for el in c:
    el.reverse()
for el in c:
    print(" ".join(el))
