s = list(input())
s.reverse()

ans = []
for el in s:
    if el == "6":
        ans.append("9")
    elif el == "9":
        ans.append("6")
    else:
        ans.append(el)

print("".join(ans))
