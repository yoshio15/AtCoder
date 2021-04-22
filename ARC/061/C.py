S = input()

ans = 0
for i in range(2 ** (len(S) - 1)):
    formula = ""
    for j in range(len(S)):
        formula += S[j]
        if (i >> j) & 1 and j != len(S) - 1:
            formula += "+"
        if j == len(S) - 1:
            ans += eval(formula)

print(ans)
