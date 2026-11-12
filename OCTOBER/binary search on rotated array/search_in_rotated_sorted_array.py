def search(nums: list[int], target: int) -> int:
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        # Check if the left half is sorted
        if nums[lo] <= nums[mid]:
            # Target lies within the sorted left half
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        # Otherwise, the right half must be sorted
        else:
            # Target lies within the sorted right half
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
print(search([4, 5, 6, 7, 0, 1, 2], 0)) 