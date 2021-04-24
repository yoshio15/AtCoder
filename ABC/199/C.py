def main():
    N = int(input())
    S = input()
    Q = int(input())
    TAB = [map(int, input().split()) for _ in range(Q)]
    T, A, B = [list(i) for i in zip(*TAB)]

    tmp_S = list(S)
    for i in range(Q):
        if T[i] == 1:
            tmp_S[B[i] - 1], tmp_S[A[i] - 1] = tmp_S[A[i] - 1], tmp_S[B[i] - 1]
        else:
        # elif T[i] == 2:
            tmp_S = tmp_S[N:] + tmp_S[:N]

    S = "".join(tmp_S)
    print(S)


main()
