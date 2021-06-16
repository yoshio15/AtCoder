r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
ans = 0
while True:
    if r1 + c1 == r2 + c2 \
            or r1 - c1 == r2 - c2 \
            or abs(r1 - r2) + abs(c1 - c2) <= 3:
        break
    # TODO 最適なところに r1, c1 を動かす
    ans += 1
print(ans)
