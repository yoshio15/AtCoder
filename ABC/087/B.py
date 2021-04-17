A = int(input())  # 500yen
B = int(input())  # 100yen
C = int(input())  # 50yen
X = int(input())  # SUM

ans = 0

for a in range(A+1):
    if 500 * a == X:
        ans += 1
    for b in range(B+1):
        if (500 * a) + (100 * b) == X:
            if b != 0:
                ans += 1
        for c in range(C+1):
            if (500 * a) + (100 * b) + (50 * c) == X:
                if c != 0:
                    ans += 1

print(ans)
