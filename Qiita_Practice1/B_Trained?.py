N = int(input())
A = [{}] * N
for i in range(N):
    A[i] = {"index": i, "num": int(input()), "didCome": False}

ans = -1
ni = 0
for i in range(N):
    if A[ni]["index"] == 1:
        ans = i
        break
    if A[ni]["didCome"]:
        break
    A[ni]["didCome"] = True
    ni = A[ni]["num"] - 1

print(ans)
