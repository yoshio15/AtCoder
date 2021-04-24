N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
a = max(A)
b = min(B)
if b - a >= 0:
    ans = b - a + 1
print(ans)
