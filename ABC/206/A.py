n = int(input())
tax = 1.08
price = int(n * tax)
ans = "Yay!"
if price == 206:
    ans = "so-so"
elif price > 206:
    ans = ":("
print(ans)
