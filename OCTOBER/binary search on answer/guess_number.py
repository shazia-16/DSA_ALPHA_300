def guessNumber(n: int, pick: int) -> int:
    lo = 1
    hi = n
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        # Condition check directly comparing mid to target
        if mid == pick:
            return mid
        elif mid > pick:
            hi = mid - 1  # Target is lower
        else:
            lo = mid + 1  # Target is higher

    return -1
print(guessNumber(10, 6)) 