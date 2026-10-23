def isPerfectSquare(num: int) -> bool:
    if num < 1:
        return False
    lo = 1
    hi = num
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        square = mid * mid

        # Condition check
        if square == num:
            return True
        elif square < num:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
print(isPerfectSquare(16)) 