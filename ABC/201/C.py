S = input()
ans = 0
for i in range(10000):
    # 0 - 9 の数値の中でどの数値が使われているかを保持
    flag = [False] * 10
    now = i
    for j in range(4):
        flag[now % 10] = True
        now //= 10
    flag2 = True
    for j in range(10):
        # o の数値が使われていなかったら NG
        if S[j] == 'o' and not flag[j]:
            flag2 = False
        # x の数値が使われていたら NG
        if S[j] == 'x' and flag[j]:
            flag2 = False
    # bool 型は int 型のサブクラス
    ans += flag2
print(ans)
