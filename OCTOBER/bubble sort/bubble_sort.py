def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
print(bubble_sort([64, 34, 25, 12, 22, 11, 90])) 