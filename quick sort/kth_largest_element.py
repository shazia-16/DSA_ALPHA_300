def find_kth_largest(nums, k):
    n = len(nums)
    target_idx = n - k  # Convert k-th largest to 0-based sorted index
    def quick_select(low, high):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        p_idx = i + 1
        if p_idx == target_idx:
            return nums[p_idx]
        elif p_idx < target_idx:
            return quick_select(p_idx + 1, high)
        else:
            return quick_select(low, p_idx - 1)

    return quick_select(0, n - 1)
print(find_kth_largest([3, 2, 1, 5, 6, 4], 2)) 