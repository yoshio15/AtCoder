n = int(input())
str_n = str(n)

ans = 0
if len(str_n) == 1:
    ans = n
else:
    tmp = ""
    for i in range(len(str_n) - 1):
        tmp += "9"
    if str_n[1:] == tmp:
        tmp = str_n[0] + tmp
    else:
        tmp = str(int(str_n[0]) - 1) + tmp
    _tmp = [int(i) for i in list(tmp)]
    ans = sum(_tmp)

print(ans)

