def length_of_longest_substring(s):
    last_seen = {}  # Char -> last index seen
    left = 0
    max_len = 0

    for right in range(len(s)):
        char = s[right]
        if char in last_seen and last_seen[char] >= left:        # If character is already in window, jump left pointer past duplicate
            left = last_seen[char] + 1
        last_seen[char] = right
        window_len = right - left + 1
        if window_len > max_len:
            max_len = window_len

    return max_len
print(length_of_longest_substring("abcabcbb")) 