def contains_nearby_duplicate(nums, k):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, min(i + k + 1, n)):
            if nums[i] == nums[j]:
                return True
    return False
print(contains_nearby_duplicate([1, 2, 3, 1], 3))  
print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))  