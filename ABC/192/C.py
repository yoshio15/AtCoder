n, k = map(int, input().split())

test = ["0", "0", "2", "4"]
print(int("".join(test)))


def g2(x):
    arr = []
    for el in list(str(x)):
        arr.append(int(el))
    arr.sort()
    arr_str = []
    for el in arr:
        arr_str.append(str(el))
    return int("".join(arr_str))


def g1(x):
    arr = []
    for el in list(str(x)):
        arr.append(int(el))
    arr.sort(reverse=True)
    arr_str = []
    for el in arr:
        arr_str.append(str(el))
    return int("".join(arr_str))


def f(x):
    return g1(x) - g2(x)


ans = 0
ans_list = []
tar = n
for i in range(k):
    tmp = f(tar)
    ans_list.append(tmp)
    ans = tmp
    if tmp == tar:
        break
    tar = tmp

print(ans)
