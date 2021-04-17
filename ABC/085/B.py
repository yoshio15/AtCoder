N = int(input())
A = [int(input()) for _ in range(N)]

bottom = 0
ans = 0

size = len(A)
for i in range(size):
    max_size = max(A)
    if i == 0 or max_size < bottom:
        ans += 1
        bottom = max_size
    A.remove(max_size)

print(ans)
