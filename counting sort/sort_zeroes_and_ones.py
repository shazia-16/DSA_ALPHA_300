def sort_zeros_and_ones(nums):
    n = len(nums)
    zero_count = 0
    # Count total zeros
    for num in nums:
        if num == 0:
            zero_count += 1
    # Overwrite in-place
    for i in range(zero_count):
        nums[i] = 0
    for i in range(zero_count, n):
        nums[i] = 1
    return nums
arr = [1, 0, 1, 0, 1, 0, 0, 1]
sort_zeros_and_ones(arr)
print(arr)  