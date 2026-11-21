def my_merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = []
    for i in range(mid):
        left_half.append(arr[i])

    right_half = []
    for i in range(mid, len(arr)):
        right_half.append(arr[i])

    left_sorted = my_merge_sort(left_half)
    right_sorted = my_merge_sort(right_half)

    merged = []
    i = 0
    j = 0
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        else:
            merged.append(right_sorted[j])
            j += 1

    while i < len(left_sorted):
        merged.append(left_sorted[i])
        i += 1
    while j < len(right_sorted):
        merged.append(right_sorted[j])
        j += 1

    return merged
def three_sum(nums: list[int]) -> list[list[int]]:
    sorted_nums = my_merge_sort(nums)
    n = len(sorted_nums)
    result = []

    for i in range(n - 2):
        if sorted_nums[i] > 0:
            break
        if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
            if total == 0:
                result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                left += 1
                right -= 1
                while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                    left += 1
                while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result