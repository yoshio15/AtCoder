n = int(input())
a, b = map(int, input().split())
k = int(input())
p = list(map(int, input().split()))
set_p = set(p)
ans = "YES"
if a in p or b in p or len(p) != len(set_p):
    ans = "NO"
print(ans)
