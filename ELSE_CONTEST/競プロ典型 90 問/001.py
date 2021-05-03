n, l = map(int, input().split())
k = int(input())
a = list(map(int, (input().split())))

li = 0
ri = 10 ** 9


def check(i):
    sp_cnt = 0
    pre = 0
    for j in range(n):
        if a[j] - pre >= i and l - a[j] >= i:
            sp_cnt += 1
            pre = a[j]
        if sp_cnt >= k:
            return True
    return False


while ri - li > 1:
    mi = (ri + li) // 2
    if check(mi):
        li = mi
    else:
        ri = mi

print(li)
