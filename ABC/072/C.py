import collections

n = int(input())
a = list(map(int, input().split()))

ans_list = []
for el in a:
    ans_list.append(el - 1)
    ans_list.append(el)
    ans_list.append(el + 1)

c = collections.Counter(ans_list)
print(max(c.values()))
