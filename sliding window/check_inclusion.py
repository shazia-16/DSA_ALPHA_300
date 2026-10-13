def check_inclusion(s1, s2):
    len_1, len_2 = len(s1), len(s2)
    if len_1 > len_2:
        return False
    s1_count = {}
    window_count = {}
    for i in range(len_1):
        s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
        window_count[s2[i]] = window_count.get(s2[i], 0) + 1

    if window_count == s1_count:
        return True
    left = 0
    for right in range(len_1, len_2):
        window_count[s2[right]] = window_count.get(s2[right], 0) + 1
        left_char = s2[left]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]
        left += 1
        if window_count == s1_count:
            return True
    return False
print(check_inclusion("ab", "eidbaooo")) 