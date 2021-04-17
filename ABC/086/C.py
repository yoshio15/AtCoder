N = int(input())
t = [0] * N
x = [0] * N
y = [0] * N
for i in range(N):
    t[i], x[i], y[i] = map(int, input().split())

ans = 'Yes'
old_t = 0
old_x = 0
old_y = 0

for i in range(N):
    if abs(x[i] - old_x) + abs(y[i] - old_y) <= t[i] - old_t:
        if y[i] % 2 == (t[i] - x[i]) % 2:
            old_t = t[i]
            old_x = x[i]
            old_y = y[i]
            if i + 1 == N:
                ans = 'Yes'
        else:
            ans = 'No'
            break
    else:
        ans = 'No'
        break

print(ans)
