def findPeakElement(nums: list[int]) -> int:
    lo = 0
    hi = len(nums) - 1

    while lo < hi:
        mid = lo + (hi - lo) // 2
        # If mid + 1 is greater, the slope is rising to the right -> peak must exist on right
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1
        # Otherwise, slope is rising/flat to the left -> peak exists on left (or mid is peak)
        else:
            hi = mid

    return lo
print(findPeakElement([1, 2, 3, 1]))  