def searchRange(nums: list[int], target: int) -> list[int]:
    def find_bound(is_first: bool) -> int:
        lo = 0
        hi = len(nums) - 1
        bound = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                bound = mid
                if is_first:
                    hi = mid - 1  # Keep searching left for first occurrence
                else:
                    lo = mid + 1  # Keep searching right for last occurrence
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return bound
    first = find_bound(is_first=True)
    if first == -1:
        return [-1, -1]
    last = find_bound(is_first=False)
    return [first, last]
print(searchRange([5, 7, 7, 8, 8, 10], 8)) 