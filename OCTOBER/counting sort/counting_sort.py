def counting_sort(nums):
    if not nums:
        return nums

    # Find min and max manually
    min_val = nums[0]
    max_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    # Create count array
    range_size = max_val - min_val + 1
    counts = [0] * range_size

    # Count frequencies
    for num in nums:
        counts[num - min_val] += 1

    # Overwrite original array in sorted order 
    pos = 0
    for i in range(range_size):
        val = i + min_val
        freq = counts[i]
        for _ in range(freq):
            nums[pos] = val
            pos += 1

    return nums
print(counting_sort([4, 2, 2, 8, 3, 3, 1]))  