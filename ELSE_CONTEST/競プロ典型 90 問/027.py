# dict に対する in はリストに対する in よりも高速
n = int(input())
r_dict = dict()
ans_list = []

for i in range(n):
    tmp = input()
    if tmp in r_dict:
        continue
    r_dict[tmp] = True
    ans_list.append(i + 1)

# print(r_dict)
for el in ans_list:
    print(el)
