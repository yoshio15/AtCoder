n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()

ans_list = []
for i in range(n):
    ans_list.append(abs(a[i] - b[i]))

print(sum(ans_list))
