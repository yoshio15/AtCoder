# TODO 累積和を使って解き直す
N = int(input())
S = input()

ec = S.count("E")
wc = S.count("W")
ans = N
for i in range(N):
    cnt = S[:i].count("W") + S[i+1:].count("E")
    if ans > cnt:
        ans = cnt

print(ans)
