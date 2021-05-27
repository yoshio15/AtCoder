from math import comb

A, B, K = map(int, input().split())
a = A  # 残っているaの数
b = B  # 残っているbの数
ans = ""

# a または b が 0 になると正しく計算できなくなるので、打ち切ります
# そして余っている文字を全部末尾にくっつけます
while a > 0 and b > 0:
    a_comb = comb(a - 1 + b, a - 1)
    if K <= a_comb:
        ans += "a"
        a -= 1
    else:
        ans += "b"
        b -= 1
        K -= a_comb
ans += "a" * a
ans += "b" * b
print(ans)
