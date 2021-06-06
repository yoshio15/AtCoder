n = int(input())
a = input().split()
ans = 0
for el in a:
    num = int(el)
    if num >= 10:
        ans += (num - 10)
print(ans)
