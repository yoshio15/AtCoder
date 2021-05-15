n = int(input())
dic = dict()
for i in range(n):
    s, t = input().split()
    t = int(t)
    dic[t] = s

dic2 = sorted(dic.items())
print(dic2[-2][1])
