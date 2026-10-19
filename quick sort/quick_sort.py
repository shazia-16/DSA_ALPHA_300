def quick_sort_hoare(nums, low, high):
    if low < high:          # partitioning   
        pivot = nums[low]
        left = low - 1
        right = high + 1

        while True:
            left += 1
            while nums[left] < pivot:
                left += 1

            right -= 1
            while nums[right] > pivot:
                right -= 1

            if left >= right:
                p_idx = right
                break

            nums[left], nums[right] = nums[right], nums[left]
        quick_sort_hoare(nums, low, p_idx)
        quick_sort_hoare(nums, p_idx + 1, high)

    return nums
arr = [10, 7, 8, 9, 1, 5]
print(quick_sort_hoare(arr, 0, len(arr) - 1)) 