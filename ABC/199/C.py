def main():
    N = int(input())
    S = input()
    Q = int(input())
    TAB = [map(int, input().split()) for _ in range(Q)]
    T, A, B = [list(i) for i in zip(*TAB)]

    tmp_S = list(S)
    is_reversed = False
    for i in range(Q):
        if T[i] == 1:
            if is_reversed:
                a = A[i] + N if A[i] < N else A[i] - N
                b = B[i] + N if B[i] < N else B[i] - N
                tmp_S[b - 1], tmp_S[a - 1] = tmp_S[a - 1], tmp_S[b - 1]
            else:
                tmp_S[B[i] - 1], tmp_S[A[i] - 1] = tmp_S[A[i] - 1], tmp_S[B[i] - 1]

        else:
            is_reversed = not is_reversed

    if is_reversed:
        tmp_S = tmp_S[N:] + tmp_S[:N]

    S = "".join(tmp_S)
    print(S)


main()
