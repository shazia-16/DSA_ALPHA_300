def character_replacement(s, k):
    left = 0
    max_len = 0
    max_freq = 0
    counts = {}  # Char -> frequency in current window

    for right in range(len(s)):
        char = s[right]
        counts[char] = counts.get(char, 0) + 1
        if counts[char] > max_freq:       # Track the highest frequency seen in the current window
            max_freq = counts[char]
        window_len = right - left + 1      # If replacements needed > k, shrink window from left
        while window_len - max_freq > k:
            left_char = s[left]
            counts[left_char] -= 1
            left += 1
            window_len = right - left + 1
        if window_len > max_len:
            max_len = window_len
    return max_len
print(character_replacement("AABABBA", 1)) 