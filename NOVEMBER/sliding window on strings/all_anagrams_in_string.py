def find_anagrams(s: str, p: str) -> list[int]:
    n, m = len(s), len(p)
    if m > n:
        return []
        
    p_freq = {}
    window_freq = {}
    
    # Initialize frequency dicts for the first window
    for i in range(m):
        p_freq[p[i]] = p_freq.get(p[i], 0) + 1
        window_freq[s[i]] = window_freq.get(s[i], 0) + 1
        
    result = []
    if window_freq == p_freq:
        result.append(0)
        
    # Slide the fixed-size window across s
    for right in range(m, n):
        in_char = s[right]
        out_char = s[right - m]
        
        window_freq[in_char] = window_freq.get(in_char, 0) + 1
        window_freq[out_char] -= 1
        
        # Clean up zero-count keys so dict equality works cleanly
        if window_freq[out_char] == 0:
            del window_freq[out_char]
            
        if window_freq == p_freq:
            result.append(right - m + 1)
            
    return result