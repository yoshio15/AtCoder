# 最小値の最大値は二分探索を用いて解く
N = int(input())
A = [tuple(map(int, input().split())) for i in range(N)]


def check(x):
    s = set()
    for a in A:
        s.add(sum(1 << i for i in range(5) if a[i] >= x))
    for x in s:
        for y in s:
            for z in s:
                if x | y | z == 31:
                    return True
    return False


ok = 0
ng = 10 ** 9 + 1
while ng - ok > 1:
    print("ok={}, ng={}".format(ok, ng))
    cen = (ok + ng) // 2
    if check(cen):
        print("cen={}, Check OK".format(cen))
        ok = cen
    else:
        print("cen={}, Check NG".format(cen))
        ng = cen
print(ok)
