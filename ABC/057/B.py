n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]

ans_list = []
for student in ab:
    min_distance = 10 ** 9
    min_check_point = -1
    for i in range(m):
        distance = abs(student[0] - cd[i][0]) + abs(student[1] - cd[i][1])
        if distance < min_distance:
            min_distance = distance
            min_check_point = i + 1
    ans_list.append(min_check_point)

for ans in ans_list:
    print(ans)
