
def lps_F(pat):
    m = len(pat)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps
def kmp(txt, pat):
    n = len(txt)
    m = len(pat)
    lps = lps_F(pat)
    i = j = 0
    while i < n:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == m:
            print(f"pattern at index {i - j}")
            j = lps[j - 1]

        elif i < n and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


