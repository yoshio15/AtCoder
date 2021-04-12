H, W = map(int, input().split())
S = []
bom = "#"
for i in range(H):
    S.append(list(input()))

for i in range(H):
    for k in range(W):
        if S[i][k] == bom:
            # skip
            continue
        else:
            # set number of bom surrounded
            bom_cnt = 0
            for m in range(3):
                if (i == 0 and m == 0) or (i+1 == H and m == 2):
                    continue
                for n in range(3):
                    if (k == 0 and n == 0) or (k+1 == W and n == 2) or (m == 1 and n == 1):
                        continue
                    if S[i-1+m][k-1+n] == bom:
                        bom_cnt += 1
                S[i][k] = bom_cnt

for s in S:
    str_list = map(str, s)
    print(''.join(str_list))
