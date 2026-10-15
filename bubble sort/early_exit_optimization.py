def bubble_sort_optimized(nums):
    n = len(nums)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums
print(bubble_sort_optimized([1, 2, 3, 4, 5]))  