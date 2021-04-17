N = int(input())
I1 = list(map(int, input().split()))
I2 = list(map(int, input().split()))

ans = 0
for i in range(N):
    total = sum(I1[:i + 1]) + sum(I2[i:])
    if total > ans:
        ans = total

print(ans)
