import itertools

n, l = map(int, input().split())
k = int(input())
a = list(map(int, (input().split())))

sep = [i for i in range(n)]
il = [i for i in range(k)]

ans = 0
for el in itertools.combinations(sep, k):
    len_l = []
    for i in il:
        len_l.append(a[el[i]])
    # print(len_l)
    p_len_l = []
    for i in range(len(len_l)):
        if i == len(len_l) - 1:
            p_len_l.append(l - len_l[i])
        if i == 0:
            p_len_l.append(len_l[i])
        else:
            p_len_l.append(len_l[i] - len_l[i - 1])
    # print(p_len_l)
    if min(p_len_l) > ans:
        ans = min(p_len_l)

print(ans)
