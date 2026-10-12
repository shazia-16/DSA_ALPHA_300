def two_sum_sorted(numbers, target):
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]  # 1-based index
    return []
print(two_sum_sorted([2, 7, 11, 15], 9)) 