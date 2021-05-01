N, D, H = map(int, input().split())
dh = [map(int, input().split()) for _ in range(N)]
d, h = [list(i) for i in zip(*dh)]

ans = 0
for i in range(N):
    # a = (h[i] - H) / (d[i] - D)
    b = H - (D * (h[i] - H) / (d[i] - D))
    if b > ans:
        ans = b

print(ans)
