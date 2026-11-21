def sorted_squares(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    write = n - 1
    
    while left <= right:
        left_sq = nums[left] * nums[left]
        right_sq = nums[right] * nums[right]
        
        if left_sq > right_sq:
            result[write] = left_sq
            left += 1
        else:
            result[write] = right_sq
            right -= 1
        write -= 1
        
    return result