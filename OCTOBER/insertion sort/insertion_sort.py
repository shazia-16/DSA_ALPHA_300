def insertion_sort(nums):
    n = len(nums)

    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:      #shift elements > key to the right
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key     #place key in corrected position

    return nums
print(insertion_sort([12, 11, 13, 5, 6]))  