import math

a, b, c = map(int, input().split())
ans = "No"
if math.log(a, 2) < b * math.log(c, 2):
    ans = "Yes"

print(ans)
