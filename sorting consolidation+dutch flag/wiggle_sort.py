def wiggleSort(nums: list[int]) -> None:
    for i in range(len(nums) - 1):
        # Even index should be <= next element
        if i % 2 == 0:
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        # Odd index should be >= next element
        else:
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
arr = [3, 5, 2, 1, 6, 4]
wiggleSort(arr)
print(arr) 