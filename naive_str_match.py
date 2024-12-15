def naive(txt, pat):
    m = len(pat)
    n = len(txt)

    for i in range(n - m + 1):
        count = 0
        for j in range(m):
            if txt[i + j] == pat[j]:
                count += 1
            else:
                break
        if count == m:
            return i

    return -1

txt = 'aaabbbababa'
pat = 'aba'
print(naive(txt, pat))
