ABCD = input()
A = int(ABCD[0])
B = int(ABCD[1])
C = int(ABCD[2])
D = int(ABCD[3])
plus = "1"
minus = "0"

ans = ""
for i in range(2 ** (len(ABCD) - 1)):
    p = "{:03b}".format(i)
    tmp_ans = A
    ans = str(A)

    if p[0] == plus:
        tmp_ans += B
        ans += "+" + str(B)
    else:
        tmp_ans -= B
        ans += "-" + str(B)

    if p[1] == plus:
        tmp_ans += C
        ans += "+" + str(C)
    else:
        tmp_ans -= C
        ans += "-" + str(C)

    if p[2] == plus:
        tmp_ans += D
        ans += "+" + str(D)
    else:
        tmp_ans -= D
        ans += "-" + str(D)

    if tmp_ans == 7:
        ans += "=7"
        break

print(ans)
