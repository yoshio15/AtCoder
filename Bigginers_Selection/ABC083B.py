N, A, B = map(int, input().split())

ans = 0

for n in range(N):
    l = [int(x) for x in list(str(n+1))]
    s = sum(l)
    if A <= s <= B:
        ans += (n+1)

print(ans)
