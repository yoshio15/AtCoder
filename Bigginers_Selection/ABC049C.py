S = input()
T = ''

answer = 'NO'
candidates = ['dream', 'dreamer', 'erase', 'eraser']
is_matched = True

while len(S) > 0:
    if not is_matched:
        break
    for c in candidates:
        # print("{} => {}：{}".format(S, c, S.endswith(c)))
        if S.endswith(c):
            S = S[:len(S)-len(c)]
            is_matched = True
            if len(S) == 0:
                answer = 'YES'
            break
        is_matched = False

print(answer)
