def first_non_repeating(nums: list[int]) -> int:
    counts = {}
    
    # First pass: build frequency map
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        
    # Second pass: find first element with frequency 1
    for num in nums:
        if counts[num] == 1:
            return num
            
    return -1  # All elements repeat