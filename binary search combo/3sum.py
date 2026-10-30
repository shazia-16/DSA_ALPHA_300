def threeSum(nums: list[int]) -> list[list[int]]:
    # Custom Merge Sort
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
    res = []
    n = len(sorted_nums)

    for i in range(n - 2):
        # Skip duplicate values for first element
        if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]

            if total == 0:
                res.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                left += 1
                right -= 1

                # Skip duplicate values for second and third elements
                while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                    left += 1
                while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return res
print(threeSum([-1, 0, 1, 2, -1, -4])) 