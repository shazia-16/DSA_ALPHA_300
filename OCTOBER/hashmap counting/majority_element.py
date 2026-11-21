def majority_element(nums: list[int]) -> int:
    counts = {}
    threshold = len(nums) // 2
    
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
            
        if counts[num] > threshold:
            return num
            
    return -1  # In case no majority element exists