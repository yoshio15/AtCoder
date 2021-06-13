a, b, c = map(int, input().split())
ans = "="

if c % 2 == 0:
    if abs(a) != abs(b):
        if abs(a) > abs(b):
            ans = ">"
        else:
            ans = "<"
else:
    if a != b:
        if a < 0 and b < 0:
            if abs(a) > abs(b):
                ans = "<"
            else:
                ans = ">"
        elif a >= 0 and b >= 0:
            if abs(a) > abs(b):
                ans = ">"
            else:
                ans = "<"
        else:
            if a < 0:
                ans = "<"
            else:
                ans = ">"

print(ans)
