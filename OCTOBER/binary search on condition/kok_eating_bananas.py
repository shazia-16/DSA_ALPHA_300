def minEatingSpeed(piles: list[int], h: int) -> int:
    lo = 1
    hi = max(piles)
    ans = hi

    # Feasibility check: Can Koko eat all bananas within 'h' hours at 'speed'?
    def can_eat_all(speed: int) -> bool:
        hours = 0
        for pile in piles:
            # Ceiling division without math.ceil: (pile + speed - 1) // speed
            hours += (pile + speed - 1) // speed
        return hours <= h
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if can_eat_all(mid):
            ans = mid
            hi = mid - 1  # Feasible -> try finding a smaller speed
        else:
            lo = mid + 1  # Infeasible -> need faster speed
    return ans
print(minEatingSpeed([3, 6, 7, 11], 8))  