A, B = map(int, input().split())

A_list = [0] * A
B_list = [0] * B
ans = [0] * (A + B)
sum_num = 0

if A >= B:
    for i in range(A):
        A_list[i] = i + 1
        sum_num += i + 1
    for i in range(B):
        if i == B - 1:
            B_list[i] = - (sum_num + sum(B_list))
        else:
            B_list[i] = - (i + 1)

if A < B:
    for i in range(B):
        sum_num += -(i + 1)
        B_list[i] = -(i + 1)
    for i in range(A):
        if i == A - 1:
            A_list[i] = - (sum_num - sum(A_list))
        else:
            A_list[i] = i + 1

ans = A_list + B_list
ans_str = " ".join([str(el) for el in ans])
print(ans_str)
