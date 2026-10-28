def shipWithinDays(weights: list[int], days: int) -> int:
    # Lower bound: must be able to carry the heaviest single package
    # Upper bound: carrying everything in 1 day
    lo = max(weights)
    hi = sum(weights)
    ans = hi

    # Feasibility check: Can we ship all packages within 'days' using 'capacity'?
    def can_ship(capacity: int) -> bool:
        needed_days = 1
        current_load = 0
        for w in weights:
            if current_load + w > capacity:
                needed_days += 1
                current_load = w
            else:
                current_load += w
        return needed_days <= days
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if can_ship(mid):
            ans = mid
            hi = mid - 1  # Feasible -> try finding a smaller capacity
        else:
            lo = mid + 1  # Infeasible -> need larger capacity
    return ans
print(shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)) 