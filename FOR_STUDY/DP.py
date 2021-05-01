# Fibonacci sequence
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...]
# フィボナッチ数列のインデックスnの位置の値を取得する処理
import functools

cnt = 0
memo = {}


# (1)全探索Ver
def fib_rec(n):
    global cnt
    cnt += 1
    print("n={}".format(n))
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


# (2)メモ化再帰Ver
def fib_mem(n):
    global cnt
    global memo
    cnt += 1
    print("n={}".format(n))
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fib_mem(n - 1) + fib_mem(n - 2)
        return memo[n]


# (3)メモ化再帰Ver2 ... こっちの方が(2)より若干早い
@functools.lru_cache(maxsize=None)
def fib_mem2(n):
    global cnt
    cnt += 1
    print("n={}".format(n))
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_mem2(n - 1) + fib_mem2(n - 2)


# (4)ボトムアップVer
def fib_bottom_up(n):
    global cnt
    cnt += 1
    ret = {0: 0, 1: 1}
    for k in range(2, n + 1):
        print(k)
        ret[k] = ret[k - 1] + ret[k - 2]
    print(ret)
    return ret[n]


i = 100
# ans = fib_rec(i)
# ans = fib_mem(i)
# ans = fib_mem2(i)
ans = fib_bottom_up(i)
print("i={}, answer={}".format(i, ans))
print(cnt)
