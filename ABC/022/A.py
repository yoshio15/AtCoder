n, s, t = map(int, input().split())
w = int(input())
a = [int(input()) for _ in range(2, n + 1)]

ans = 0
if s <= w <= t:
    ans += 1

yesterday_w = w
for el in a:
    today_w = yesterday_w + el
    if s <= today_w <= t:
        ans += 1
    yesterday_w = today_w

print(ans)

