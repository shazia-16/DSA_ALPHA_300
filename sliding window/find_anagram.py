def find_anagrams(s, p):
    len_s, len_p = len(s), len(p)
    if len_p > len_s:
        return []
    p_count = {}
    s_count = {}
    for i in range(len_p):   #initialize the character count for p and the first window of s
        p_count[p[i]] = p_count.get(p[i], 0) + 1
        s_count[s[i]] = s_count.get(s[i], 0) + 1
    result = [None] * len_s
    res_count = 0

    if s_count == p_count:
        result[res_count] = 0
        res_count += 1
    left = 0                     #sliding windwow
    for right in range(len_p, len_s):
        # Add incoming right character
        s_count[s[right]] = s_count.get(s[right], 0) + 1
        left_char = s[left]
        s_count[left_char] -= 1
        if s_count[left_char] == 0:
            del s_count[left_char]

        left += 1
        if s_count == p_count:
            result[res_count] = left
            res_count += 1
    return result[:res_count]
print(find_anagrams("cbaebabacd", "abc"))