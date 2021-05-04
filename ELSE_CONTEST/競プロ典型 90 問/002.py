import collections
import copy

n = int(input())
ans_list = []

bs = "("  # 1
be = ")"  # 0


# カッコの対応関係が正しければ True を返却する
def isOkBracket(bl):
    # カッコの対応関係を一時的に保持するスタック
    stack = collections.deque()
    while len(bl) > 0:
        target = bl.popleft()
        if target == bs:
            stack.appendleft(target)
        else:
            if len(stack) > 0:
                stack.popleft()
            else:
                return False
    return True


# Nが奇数の場合は必ず正しいカッコ列にはならない
if n % 2 == 0:
    candidate_list = []
    for i in range(2 ** n):
        brackets_list = collections.deque()
        for j in range(n):
            # フラグが立っていたら "(" 、立っていなければ ")" とする
            if (i >> j) & 1:
                brackets_list.appendleft(bs)
            else:
                brackets_list.appendleft(be)
        # "(" と ")" の数が一致しているもののみ候補IN
        if brackets_list.count(bs) == n // 2:
            if isOkBracket(copy.copy(brackets_list)):
                ans_list.append(list(brackets_list))

ans_list.sort()
for ans in ans_list:
    print("".join(ans))
