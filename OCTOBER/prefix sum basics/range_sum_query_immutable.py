class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix = [0]
        current_sum = 0
        for num in nums:
            current_sum += num
            self.prefix.append(current_sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]