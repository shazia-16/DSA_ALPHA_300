def peakIndexInMountainArray(arr: list[int]) -> int:
    lo = 0
    hi = len(arr) - 1

    while lo < hi:
        mid = lo + (hi - lo) // 2
        # Slope is rising -> peak is to the right
        if arr[mid] < arr[mid + 1]:
            lo = mid + 1
        # Slope is falling -> peak is at mid or to the left
        else:
            hi = mid

    return lo
print(peakIndexInMountainArray([0, 1, 0]))