import collections

n, k = map(int, input().split())
c = list(map(int, input().split()))
ans = 1
# for i in range(n - k + 1):
#     tmp = len(set(c[i:i + k]))
#     if tmp > ans:
#         ans = tmp
queue = collections.deque()
for i in range(k):
    queue.append(c[i])
for i in range(n - k):
    # print(queue)
    tmp = len(set(queue))
    if tmp > ans:
        ans = tmp
    queue.append(c[i + k])
    queue.popleft()
print(ans)
