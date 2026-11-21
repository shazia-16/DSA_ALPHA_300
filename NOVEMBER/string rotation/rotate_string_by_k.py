def rotate_string_by_k(s: str, k: int) -> str:
    n = len(s)
    if n == 0:
        return ""

    # Normalize rotation amount k
    k = k % n
    if k == 0:
        return s

    # Build character list manually starting from the shifted start position
    chars = []
    
    # The new start of the string after right rotation by k is at index (n - k)
    start_idx = n - k
    
    for i in range(n):
        curr_idx = (start_idx + i) % n
        chars.append(s[curr_idx])

    # Join character array into a string manually
    result = ""
    for ch in chars:
        result += ch

    return result
print(rotate_string_by_k("srmalpha", 3)) 