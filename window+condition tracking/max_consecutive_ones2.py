def longest_ones(nums, k):
    left = 0
    zero_count = 0
    max_len = 0
    for right in range(len(nums)):  
        if nums[right] == 0:    # If current element is 0, increment zero_count
            zero_count += 1
        while zero_count > k:         # Shrink window if 0s exceed k
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        window_len = right - left + 1 # Calculate current valid window size
        if window_len > max_len:
            max_len = window_len
    return max_len
print(longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)) 