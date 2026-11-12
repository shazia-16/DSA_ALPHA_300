# Note: On platforms like LeetCode, MountainArray is an interface object.
# Below is the algorithmic implementation using direct array access for local execution.

def findInMountainArray(target: int, mountain_arr: list[int]) -> int:
    n = len(mountain_arr)

    # 1. Find peak index
    lo, hi = 0, n - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if mountain_arr[mid] < mountain_arr[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    peak = lo

    # 2. Binary search on strictly increasing left slope [0, peak]
    lo, hi = 0, peak
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        val = mountain_arr[mid]
        if val == target:
            return mid
        elif val < target:
            lo = mid + 1
        else:
            hi = mid - 1

    # 3. Binary search on strictly decreasing right slope [peak + 1, n - 1]
    lo, hi = peak + 1, n - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        val = mountain_arr[mid]
        if val == target:
            return mid
        elif val > target:  # Decreasing order comparison reversed
            lo = mid + 1
        else:
            hi = mid - 1

    return -1
print(findInMountainArray(3, [1, 2, 3, 4, 5, 3, 1])) 