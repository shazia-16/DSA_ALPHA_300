def k_smallest_elements(nums, k):
    n = len(nums)
    for i in range(min(k, n)):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums[:k]
print(k_smallest_elements([7, 10, 4, 3, 20, 15], 3)) 