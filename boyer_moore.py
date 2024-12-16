def bad_character_heuristic(pattern):
    m = len(pattern)
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i
    return bad_char

def good_suffix_heuristic(pattern):
    m = len(pattern)
    suffix = [0] * m
    prefix = [False] * m
    
    for i in range(m - 1, -1, -1):
        j = i
        while j >= 0 and pattern[j] == pattern[m - 1 - i + j]:
            j -= 1
        suffix[i] = j + 1

    for i in range(m - 1):
        if suffix[i] == i + 1:
            prefix[i] = True

    return suffix, prefix

def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0 or n == 0:
        return -1
    
    bad_char = bad_character_heuristic(pattern)
    suffix, prefix = good_suffix_heuristic(pattern)
    
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            bc_shift = j - bad_char.get(text[s + j], -1)
            gs_shift = 0
            if j < m - 1:
                gs_shift = m - suffix[j + 1]
            s += max(bc_shift, gs_shift)

    return -1


