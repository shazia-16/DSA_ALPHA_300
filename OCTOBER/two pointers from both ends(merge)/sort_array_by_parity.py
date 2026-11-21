def sort_array_by_parity(nums: list[int]) -> list[int]:
    left = 0
    right = len(nums) - 1
    
    while left < right:
        while left < right and nums[left] % 2 == 0:
            left += 1
        while left < right and nums[right] % 2 == 1:
            right -= 1
            
        if left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1
            
    return nums