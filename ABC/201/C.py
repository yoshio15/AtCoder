import collections
import math

s = input()
ans = 0
cnt = collections.Counter(s)

print(cnt)
o_cnt = cnt["o"]
q_cnt = cnt["?"]

pa_a = 1
pa_b = 14
pa_c = 36
pa_d = 72

if o_cnt <= 4 or cnt["x"] == 10:
    ans = math.factorial(o_cnt)

print(ans)
