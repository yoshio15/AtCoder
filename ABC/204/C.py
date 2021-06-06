import collections
n, m = map(int, input().split())
ans = 0
dest = dict()
for i in range(n):
    dest[i + 1] = set()
for i in range(m):
    a, b = map(int, input().split())
    dest[a].add(b)
for i in range(n):
    tmp = collections.deque()
    for el in dest[i + 1]:
        tmp.append(el)
    visited_list = set()
    visited_list.add(i + 1)
    while len(tmp) > 0:
        tar = tmp.pop()
        visited_list.add(tar)
        for el in dest[tar]:
            if el not in visited_list:
                tmp.append(el)
    ans += len(visited_list)
print(ans)
