def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    n = len(numbers)

    for i in range(n - 1):
        complement = target - numbers[i]
        lo = i + 1
        hi = n - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if numbers[mid] == complement:
                return [i + 1, mid + 1]
            elif numbers[mid] < complement:
                lo = mid + 1
            else:
                hi = mid - 1

    return []