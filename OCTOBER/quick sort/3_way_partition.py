def quick_sort_3way(nums, low, high):
    if low >= high:
        return nums
    pivot = nums[low]
    lt = low
    i = low + 1
    gt = high
    while i <= gt:
        if nums[i] < pivot:
            nums[lt], nums[i] = nums[i], nums[lt]
            lt += 1
            i += 1
        elif nums[i] > pivot:
            nums[i], nums[gt] = nums[gt], nums[i]
            gt -= 1
        else:
            i += 1
    quick_sort_3way(nums, low, lt - 1)
    quick_sort_3way(nums, gt + 1, high)

    return nums
arr = [4, 9, 4, 4, 1, 9, 4, 3, 2, 1]
print(quick_sort_3way(arr, 0, len(arr) - 1)) 