import collections

n = int(input())
s = [input() for _ in range(n)]
ans_dict = collections.Counter(s)
print("AC x {}".format(ans_dict["AC"]))
print("WA x {}".format(ans_dict["WA"]))
print("TLE x {}".format(ans_dict["TLE"]))
print("RE x {}".format(ans_dict["RE"]))
