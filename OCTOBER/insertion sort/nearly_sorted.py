def sort_nearly_sorted(nums, k):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums
print(sort_nearly_sorted([6, 5, 3, 2, 8, 10, 9], 2)) 