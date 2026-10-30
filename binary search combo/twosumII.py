def twoSum(numbers: list[int], target: int) -> list[int]:
    # Using Binary Search for each complement without bisect
    def custom_binary_search(lo: int, hi: int, key: int) -> int:
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if numbers[mid] == key:
                return mid
            elif numbers[mid] < key:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
    for i in range(len(numbers)):
        needed = target - numbers[i]
        # Search for needed value in the sub-array to the right of index i
        idx = custom_binary_search(i + 1, len(numbers) - 1, needed)
        if idx != -1:
            # Return 1-based indices
            return [i + 1, idx + 1]
    return []
print(twoSum([2, 7, 11, 15], 9))  