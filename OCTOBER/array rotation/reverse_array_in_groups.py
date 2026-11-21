def reverse_in_groups(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    if k <= 1 or n <= 1:
        return nums

    for i in range(0, n, k):
        left = i
        right = i + k - 1
        if right >= n:
            right = n - 1

        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1

    return nums