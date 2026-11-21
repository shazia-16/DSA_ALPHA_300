def max_sum_subarray_k(nums: list[int], k: int) -> int:
    if len(nums) < k or k <= 0:
        return 0
        
    window_sum = 0
    for i in range(k):
        window_sum += nums[i]
        
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
            
    return max_sum