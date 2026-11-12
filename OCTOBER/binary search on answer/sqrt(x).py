def mySqrt(x: int) -> int:
    if x < 2:
        return x
    lo = 1
    hi = x // 2
    ans = 0
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        # Condition check: mid * mid <= x
        if mid * mid <= x:
            ans = mid
            lo = mid + 1  # Try finding a larger valid integer
        else:
            hi = mid - 1
    return ans
print(mySqrt(4)) 