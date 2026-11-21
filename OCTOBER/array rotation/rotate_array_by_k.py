def reverse_segment(nums: list[int], left: int, right: int) -> None:
    while left < right:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1

def rotate_left(nums: list[int], k: int) -> None:
    n = len(nums)
    if n == 0:
        return
    k = k % n
    if k == 0:
        return

    reverse_segment(nums, 0, k - 1)
    reverse_segment(nums, k, n - 1)
    reverse_segment(nums, 0, n - 1)