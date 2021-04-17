N, S = map(int, input().split())

x = -1  # 10000yen
y = -1  # 5000yen
z = -1  # 1000yen
hasAns = False

if 10000 * N >= S >= 1000 * N:

    N += 1
    for X in range(N):
        if hasAns:
            break
        for Y in range(N-X):
            Z = (N - 1) - X - Y
            # print("X={}, Y{}, Z={}の時".format(X, Y, Z))
            if (10000 * X) + (5000 * Y) + (1000 * Z) == S:
                # print("ANSWER: X={}, Y{}, Z={}".format(X, Y, Z))
                x = X
                y = Y
                z = Z
                hasAns = True
                break
        if hasAns:
            break

print("{} {} {}".format(x, y, z))
