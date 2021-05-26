import collections

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a_cnt = collections.Counter(a)

ans = 0
for el in c:
    ans += a_cnt[b[el - 1]]

print(ans)
