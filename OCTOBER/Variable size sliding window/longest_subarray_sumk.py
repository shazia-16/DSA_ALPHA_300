def longest_subarray_with_sum_k(nums, k):
    n = len(nums)
    left = 0
    current_sum = 0
    max_len = 0
    for right in range(n):
        current_sum += nums[right]
        while left <= right and current_sum > k:
            current_sum -= nums[left]
            left += 1
        if current_sum == k:
            window_len = right - left + 1
            if window_len > max_len:
                max_len = window_len
    return max_len
print(longest_subarray_with_sum_k([10, 5, 2, 7, 1, 9], 15)) 