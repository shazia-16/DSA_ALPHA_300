def searchRange(nums: list[int], target: int) -> list[int]:
    # Custom bisect_left: finds the first index where val >= target
    def custom_bisect_left(arr: list[int], val: int) -> int:
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] < val:
                lo = mid + 1
            else:
                hi = mid
        return lo
    # Custom bisect_right: finds the first index where val > target
    def custom_bisect_right(arr: list[int], val: int) -> int:
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] <= val:
                lo = mid + 1
            else:
                hi = mid
        return lo
    left_idx = custom_bisect_left(nums, target)
    if left_idx == len(nums) or nums[left_idx] != target:    # Check if target actually exists in nums
        return [-1, -1]
    right_idx = custom_bisect_right(nums, target) - 1
    return [left_idx, right_idx]
print(searchRange([5, 7, 7, 8, 8, 10], 8)) 