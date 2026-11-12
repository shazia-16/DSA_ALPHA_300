def sort_array_by_parity(nums):
    n = len(nums)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            # If current is odd and next is even, swap them
            if nums[j] % 2 != 0 and nums[j + 1] % 2 == 0:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums
print(sort_array_by_parity([3, 1, 2, 4]))  