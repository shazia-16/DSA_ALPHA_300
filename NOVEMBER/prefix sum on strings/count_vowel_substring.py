def count_vowel_substrings(word: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    freq = {}
    total = 0
    left = 0
    mid = 0
    
    for right in range(len(word)):
        ch = word[right]
        if ch not in vowels:
            # Reset window on consonant
            freq = {}
            left = right + 1
            mid = right + 1
            continue
            
        freq[ch] = freq.get(ch, 0) + 1
        
        # Shrink from mid until window [mid..right] no longer has all 5 vowels
        while len(freq) == 5:
            mid_ch = word[mid]
            freq[mid_ch] -= 1
            if freq[mid_ch] == 0:
                del freq[mid_ch]
            mid += 1
            
        # Every index from left to (mid - 1) forms a valid vowel substring ending at right
        total += mid - left
        
    return total