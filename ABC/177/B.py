s = input()
t = input()

ans = 1001
for start in range(len(s) - len(t) + 1):
    diff = 0
    for i in range(len(t)):
        if s[start + i] != t[i]:
            diff += 1
    if diff < ans:
        ans = diff

print(ans)
