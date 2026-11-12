def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0

    # Custom Merge Sort implementation
    def merge_sort(arr: list[int]) -> list[int]:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        sorted_arr = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1

        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        return sorted_arr

    sorted_nums = merge_sort(nums)

    longest = 1
    current_streak = 1

    for i in range(1, len(sorted_nums)):
        # Skip duplicates
        if sorted_nums[i] == sorted_nums[i - 1]:
            continue

        # Check for consecutive element
        if sorted_nums[i] == sorted_nums[i - 1] + 1:
            current_streak += 1
        else:
            longest = max(longest, current_streak)
            current_streak = 1

    return max(longest, current_streak)
print(longestConsecutive([100, 4, 200, 1, 3, 2]))