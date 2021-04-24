import collections

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [list(input()) for _ in range(R)]

wall = "#"
way = "."

print(c)
queue = collections.deque()
for i in range(R):
    print("----------")
    for k in range(C):
        print(c[i][k])
        if i == sy - 1 and k == sx - 1:
            print("Start Point")
