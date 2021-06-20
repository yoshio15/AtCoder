n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
ans = "No"
for i in range(n):
    print("========================")
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            print("i = {}, j = {}, k = {}".format(i, j, k))
            a = xy[i]
            b = xy[j]
            c = xy[k]
            ab = a[1] - b[1] / a[0] - b[0]
            bc = b[1] - c[1] / b[0] - c[0]
            if ab == bc:
                ans = "Yes"
                break
print(ans)
