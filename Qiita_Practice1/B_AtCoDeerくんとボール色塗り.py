N, K = map(int, input().split())

ans = 0
for i in range(N):
    if i == 0:
        ans = K
    else:
        ans *= (K - 1)

print(ans)
