s = list(input())
k = int(input())
one_cnt = 0
num = "1"
ans = "1"
for el in s:
    if el == "1":
        one_cnt += 1
        continue
    num = el
    break
if k > one_cnt:
    ans = num
print(ans)
