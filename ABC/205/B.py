n = int(input())
a = list(map(int, input().split()))
tmp = []
for i in range(n):
    tmp.append(i + 1)
a.sort()
ans = "No"
if tmp == a:
    ans = "Yes"
print(ans)
