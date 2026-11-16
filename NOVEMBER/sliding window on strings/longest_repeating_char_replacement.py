def character_replacement(s: str, k: int) -> int:
    freq = {}
    left = 0
    max_freq = 0
    max_len = 0
    
    for right in range(len(s)):
        ch = s[right]
        freq[ch] = freq.get(ch, 0) + 1
        if freq[ch] > max_freq:
            max_freq = freq[ch]
            
        # If replacements needed exceed k, slide left pointer forward
        while (right - left + 1) - max_freq > k:
            left_ch = s[left]
            freq[left_ch] -= 1
            left += 1
            
        curr_len = right - left + 1
        if curr_len > max_len:
            max_len = curr_len
            
    return max_len