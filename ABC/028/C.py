import itertools

abcde = list(map(int, input().split()))
sum_list = []
for el in itertools.combinations(abcde, 3):
    sum_list.append(sum(el))
sum_list.sort(reverse=True)
print(sum_list[2])
