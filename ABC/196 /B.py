x = input()
dot_point = x.find(".")
if dot_point != -1:
    x = x[0:dot_point]
print(int(x))
