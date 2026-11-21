def move_zeroes(nums: list[int]) -> None:
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            temp = nums[write]
            nums[write] = nums[read]
            nums[read] = temp
            write += 1