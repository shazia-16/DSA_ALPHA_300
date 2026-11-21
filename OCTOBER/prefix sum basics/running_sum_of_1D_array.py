def running_sum(nums: list[int]) -> list[int]:
    if not nums:
        return []
        
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[i - 1] + nums[i])
        
    return prefix