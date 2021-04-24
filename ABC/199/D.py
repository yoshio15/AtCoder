N, M = map(int, input().split())

if M > 0:
    AB = [map(int, input().split()) for _ in range(M)]
    A, B = [list(i) for i in zip(*AB)]

E = [{}] * N
for i in range(N):
    E[i] = {"this": i + 1, "to": [], "color": ["R", "G", "B"]}

if M > 0:
    for i in range(M):
        E[A[i] - 1]["to"].append(B[i])
        E[B[i] - 1]["to"].append(A[i])

ans = 1
for el in E:
    print(el)
    ans *= len(el["color"])

print(ans)
