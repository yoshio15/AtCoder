import collections
s = list(input())
mod = 10 ** 9 + 7
ans = 0
cnt = collections.Counter(s)
print(cnt)
for i in range(len(s)):
    if s[i] == 'c':
        for j in range(i + 1, len(s)):
            if s[j] == 'h':
                for k in range(j + 1, len(s)):
                    if s[k] == 'o':
                        for l in range(k + 1, len(s)):
                            if s[l] == 'k':
                                for m in range(l + 1, len(s)):
                                    if s[m] == 'u':
                                        for n in range(m + 1, len(s)):
                                            if s[n] == 'd':
                                                for o in range(n + 1, len(s)):
                                                    if s[o] == 'a':
                                                        for p in range(o + 1, len(s)):
                                                            if s[p] == 'i':
                                                                ans += 1
print(ans % mod)
