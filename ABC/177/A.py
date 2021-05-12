d, t, s = map(int, input().split())

ans = "No"

if t * s >= d:
    ans = "Yes"

print(ans)
