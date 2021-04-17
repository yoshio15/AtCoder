# TODO ビット演算がよく分からん
N = int(input())
A = list(map(int, input().split()))

ans_list = [0] * (N - 1)
for i in range(N - 1):
    left = A[:i + 1]
    right = A[i + 1:]
    left_or = 0
    right_or = 0
    for el in left:
        left_or |= el
    for el in right:
        right_or |= el
    ans_list[i] = left_or ^ right_or

print(min(ans_list))
