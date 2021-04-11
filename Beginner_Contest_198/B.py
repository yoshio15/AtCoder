N = input()
ans = 'No'

while N.endswith('0'):
    N = N[:-1]
_N = N[::-1]
if N == _N:
    ans = 'Yes'

print(ans)
