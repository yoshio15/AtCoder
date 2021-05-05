n = int(input())
a = list(map(int, input().split()))
a.sort()  # 昇順にソートしておく
q = int(input())
b = [int(input()) for _ in range(q)]

ans_list = []


def check(i, target):
    return a[i] > target


for student_rate in b:
    li = 0
    ri = len(a) - 1
    while ri - li > 1:
        mi = (li + ri) // 2
        if check(mi, student_rate):
            ri = mi
        else:
            li = mi
    ans_list.append(str(min(abs(a[li] - student_rate), abs(a[ri] - student_rate))))

print("\n".join(ans_list))
