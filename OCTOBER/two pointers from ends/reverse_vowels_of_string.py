def reverse_vowels(s: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    chars = []
    for ch in s:
        chars.append(ch)
        
    left = 0
    right = len(chars) - 1
    
    while left < right:
        while left < right and chars[left] not in vowels:
            left += 1
        while left < right and chars[right] not in vowels:
            right -= 1
            
        temp = chars[left]
        chars[left] = chars[right]
        chars[right] = temp
        
        left += 1
        right -= 1
        
    result = ""
    for ch in chars:
        result += ch
    return result