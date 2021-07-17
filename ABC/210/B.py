n = int(input())
s = list(input())
ans = ""
for i in range(n):
    if s[i] == "1":
        if (i + 1) % 2 == 0:
            ans = "Aoki"
        else:
            ans = "Takahashi"
        break
print(ans)
