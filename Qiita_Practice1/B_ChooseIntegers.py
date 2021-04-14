A, B, C = map(int, input().split())

ans = 'NO'
n = A
while True:
    if A > n * B:
        break
    elif A % B == C:
        ans = 'YES'
        break
    else:
        A += n

print(ans)
