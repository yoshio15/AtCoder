import time

target = int(input())
data = [i + 1 for i in range(12345678)]

# 二分探索
cnt = 0
li = 0
ri = len(data) - 1
start = time.time()
while li <= ri:
    cnt += 1
    mi = (li + ri) // 2
    if data[mi] == target:
        print("Target Index: {}".format(mi))
        break
    elif data[mi] < target:
        li = mi + 1
        continue
    else:
        ri = mi - 1
        continue
end = time.time()
print("[二分探索] TIME: {}[sec], COUNT: {}[回]".format(round(end - start, 4), cnt))

# シンプル全探索
cnt = 0
start = time.time()
for i in range(len(data)):
    cnt += 1
    if data[i] == target:
        print("Target Index: {}".format(i))
        break
end = time.time()
print("[全探索] TIME: {}[sec], COUNT: {}[回]".format(round(end - start, 4), cnt))
