def findFloorAndCeil(nums: list[int], x: int) -> list[int]:
    def custom_bisect_left(arr: list[int], val: int) -> int:     # Custom bisect_left to locate the ceiling candidate
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] < val:
                lo = mid + 1
            else:
                hi = mid
        return lo
    idx = custom_bisect_left(nums, x)
    ceil_val = nums[idx] if idx < len(nums) else -1          # Ceiling is at nums[idx] if idx < len(nums)
    if idx < len(nums) and nums[idx] == x:           # Floor is at nums[idx] if exact match, otherwise nums[idx - 1] if idx > 0
        floor_val = nums[idx]
    elif idx > 0:
        floor_val = nums[idx - 1]
    else:
        floor_val = -1
    return [floor_val, ceil_val]
print(findFloorAndCeil([1, 2, 8, 10, 10, 12, 19], 5)) 