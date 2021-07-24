s = set()
s.add(input())
s.add(input())
s.add(input())
s.add(input())
ans = "Yes"
if len(s) != 4:
    ans = "No"
print(ans)
