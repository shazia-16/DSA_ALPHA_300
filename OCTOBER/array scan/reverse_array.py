def reverse_array(nums: list[int]) -> list[int]:
    left = 0
    right = len(nums) - 1
    
    while left < right:
        # Swap elements manually
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        
        left += 1
        right -= 1
        
    return nums