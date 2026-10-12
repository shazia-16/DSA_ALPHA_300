def min_sub_array_len(target, nums):
    n = len(nums)
    left = 0
    current_sum = 0
    min_len = float("inf")
    for right in range(n):
        current_sum += nums[right]
        while current_sum >= target:
            window_len = right - left + 1
            if window_len < min_len:
                min_len = window_len
            current_sum -= nums[left]
            left += 1
    return 0 if min_len == float("inf") else min_len
print(min_sub_array_len(7, [2, 3, 1, 2, 4, 3])) 