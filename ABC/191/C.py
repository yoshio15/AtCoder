h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = 0
'''
2 * 2 マスに注目。
その 4 マスの中に "#" が 1 or 3 個ある時、その部分が頂点となる。 
また、その 4 マスの中に "#" が 0, 2, 4 個ある時、その部分は頂点とはなり得ない。
'''
for i in range(h - 1):
    for j in range(w - 1):
        cnt = 0
        for m in range(2):
            for n in range(2):
                if s[i + m][j + n] == "#":
                    cnt += 1
        if cnt == 1 or cnt == 3:
            ans += 1
print(ans)
