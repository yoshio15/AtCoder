from collections import deque

s = list(input())
t = deque()

is_rev = False
for el in s:
    if el == "R":
        is_rev = not is_rev
    elif is_rev:
        if t and t[0] == el:
            t.popleft()
        else:
            t.appendleft(el)
    else:
        if t and t[-1] == el:
            t.pop()
        else:
            t.append(el)

if is_rev:
    t.reverse()

print("".join(t))
