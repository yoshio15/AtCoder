import itertools

N = int(input())
L = list(map(int, input().split()))

ans = 0
if len(L) < 3:
    print(ans)
    exit(0)


def has_duplicates(seq):
    unique_list = []
    for el in seq:
        if el not in unique_list:
            unique_list.append(el)
    return len(seq) != len(unique_list)


for i in itertools.combinations(L, 3):
    if has_duplicates(i):
        continue
    else:
        a = i[0]
        b = i[1]
        c = i[2]
        if a < b + c and b < a + c and c < b + c:
            ans += 1

print(ans)
