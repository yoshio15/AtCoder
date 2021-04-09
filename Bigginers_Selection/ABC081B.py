N = int(input())
list1 = list(map(int, input().split()))

a = 0
flg = False
while True:
    for i in range(len(list1)):
        if list1[i] % 2 == 1:
            flg = True
            break
        else:
            list1[i] = list1[i] / 2
    if flg:
        break
    else:
        a += 1
print(a)
