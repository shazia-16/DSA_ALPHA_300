def countOccurrences(nums: list[int], target: int) -> int:
    def custom_bisect_left(arr: list[int], val: int) -> int:
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] < val:
                lo = mid + 1
            else:
                hi = mid
        return lo
    def custom_bisect_right(arr: list[int], val: int) -> int:
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] <= val:
                lo = mid + 1
            else:
                hi = mid
        return lo
    first = custom_bisect_left(nums, target)
    last = custom_bisect_right(nums, target)
    return last - first
print(countOccurrences([1, 1, 2, 2, 2, 2, 3], 2)) 