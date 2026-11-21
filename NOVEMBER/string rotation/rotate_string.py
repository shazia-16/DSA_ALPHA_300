def rotate_string(s: str, goal: str) -> bool:
    n = len(s)
    if n != len(goal):
        return False
    if n == 0:
        return True

    # Try every possible shift count `shift`
    for shift in range(n):
        match = True
        for i in range(n):
            # Check character position using modular arithmetic instead of string concatenation
            if s[(i + shift) % n] != goal[i]:
                match = False
                break
        if match:
            return True

    return False
print(rotate_string("abcde", "cdeab")) 