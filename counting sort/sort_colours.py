def sort_colors(nums):
    # Fixed count array for values 0, 1, and 2
    counts = [0, 0, 0]
    for num in nums:
        counts[num] += 1
    # Overwrite nums in-place
    pos = 0
    for val in range(3):
        freq = counts[val]
        for _ in range(freq):
            nums[pos] = val
            pos += 1
    return nums
arr = [2, 0, 2, 1, 1, 0]
sort_colors(arr)
print(arr) 