def find_max(nums: list[int]) -> int:
    if not nums:
        raise ValueError("Array cannot be empty")
        
    current_max = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > current_max:
            current_max = nums[i]
            
    return current_max