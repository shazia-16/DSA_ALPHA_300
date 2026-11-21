def find_second_largest(nums: list[int]) -> int:
    if len(nums) < 2:
        return -1  # Or raise an error if no second largest exists
        
    first = None
    second = None
    
    for num in nums:
        if first is None or num > first:
            second = first
            first = num
        elif num != first and (second is None or num > second):
            second = num
            
    return second if second is not None else -1