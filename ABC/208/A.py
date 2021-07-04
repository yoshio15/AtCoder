a, b = map(int, input().split())
ans = "No"
if 1 * a <= b <= 6 * a:
    ans = "Yes"
print(ans)
