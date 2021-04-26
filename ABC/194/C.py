# https://note.com/taraba_kanico/n/n8aca58bcd303
import itertools

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in itertools.combinations(A, 2):
    ans += (i[0] - i[1]) ** 2

print(ans)
