def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_half = merge_sort(nums[:mid])
    right_half = merge_sort(nums[mid:])
    merged = [None] * len(nums)
    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            merged[k] = left_half[i]
            i += 1
        else:
            merged[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        merged[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):     #place remaining elements from right half
        merged[k] = right_half[j]
        j += 1
        k += 1

    return merged
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))  