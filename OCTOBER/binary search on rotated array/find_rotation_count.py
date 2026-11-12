def countRotations(nums: list[int]) -> int:
    lo = 0
    hi = len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        # Right half contains the minimum / pivot
        if nums[mid] > nums[hi]:
            lo = mid + 1
        # Pivot is at mid or in the left half
        else:
            hi = mid
    return lo
print(countRotations([15, 18, 2, 3, 6, 12])) 