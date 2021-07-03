n = list(input())
n_num = [int(el) for el in n]
ans = "No"
if sum(n_num) % 9 == 0:
    ans = "Yes"
print(ans)
