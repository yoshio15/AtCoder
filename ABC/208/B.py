import math

p = int(input())
cnt = 0


def cnt_change(num):
    global p
    global cnt
    fac = math.factorial(num)
    while p >= fac:
        cnt += 1
        p -= fac


for i in range(10):
    cnt_change(10 - i)
print(cnt)
