import itertools

S1 = list(input())
S2 = list(input())
S3 = list(input())
S1_len = len(S1)
S2_len = len(S2)
S3_len = len(S3)
num = list('0123456789')
no_ans = 'UNSOLVABLE'
N1_li = [0] * S1_len
N2_li = [0] * S2_len
N3_li = [0] * S3_len
S1_first = S1[0]
S2_first = S2[0]
S3_first = S3[0]

use_char_list = set(S1 + S2 + S3)
if len(use_char_list) > 10:
    print(no_ans)
    exit(0)

char_num_dict = {}
for c in use_char_list:
    char_num_dict[c] = 0

for i in itertools.permutations(range(10), len(use_char_list)):
    print(i)
    for k in i:
        print(k)

print(char_num_dict)
