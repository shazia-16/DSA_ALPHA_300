def vowel_strings_ranges(s: str, queries: list[list[int]]) -> list[int]:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    n = len(s)
    
    # Build prefix count array manually
    prefix = [0] * (n + 1)
    for i in range(n):
        is_vowel = 1 if s[i] in vowels else 0
        prefix[i + 1] = prefix[i] + is_vowel
        
    results = []
    for left, right in queries:
        results.append(prefix[right + 1] - prefix[left])
        
    return results