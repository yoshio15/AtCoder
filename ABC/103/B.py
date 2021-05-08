import collections

s = input()
t = input()

ans = "No"

# Check letters
if collections.Counter(list(s)) == collections.Counter(list(t)):
    for i in range(len(s)):
        if s == t:
            ans = "Yes"
            break
        # Switch each letter
        s = s[len(s) - 1] + s[:len(s) - 1]

print(ans)
