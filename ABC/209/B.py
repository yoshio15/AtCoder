n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = "No"
tot = sum(a) - (len(a) // 2)
if tot <= x:
    ans = "Yes"
print(ans)
