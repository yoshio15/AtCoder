s = list(input())
t = []
R = "R"

is_rd = False
for el in s:
    if el == R:
        is_rd = not is_rd
        # t.reverse()
    else:
        if is_rd:
            t.insert(0, el)
        else:
            t.append(el)

if is_rd:
    t.reverse()

# print("".join(t))
isDone = False
while not isDone:
    bef = ""
    if len(t) == 0:
        break
    for i in range(len(t)):
        # print("".join(t))
        if i == 0:
            bef = t[i]
            continue
        if bef == t[i]:
            del_i = []
            fir = t[:i]
            las = t[i:]
            las.reverse()
            if len(fir) >= len(las):
                for k in range(len(las)):
                    print(del_i)
                    if fir[k] == las[k]:
                        del_i.append(i + k)
                        del_i.append(i - k - 1)
                        continue
                    else:
                        break
            else:
                print(t)
                for k in range(len(fir)):
                    print(del_i)
                    if fir[k] == las[k]:
                        del_i.append(i + k)
                        del_i.append(i - k - 1)
                        continue
                    else:
                        break
            del_i = sorted(del_i, reverse=True)
            print(del_i)
            for di in del_i:
                del t[di]
            break

        else:
            if i == len(t) - 1:
                isDone = True
                break
            bef = t[i]
            continue

print("".join(t))
