def count_inversions(nums):
    def merge_and_count(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, left_inv = merge_and_count(arr[:mid])
        right, right_inv = merge_and_count(arr[mid:])

        merged = [None] * len(arr)
        i = 0
        j = 0
        k = 0
        inversions = left_inv + right_inv

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged[k] = left[i]
                i += 1
            else:
                merged[k] = right[j]
                inversions += len(left) - i
                j += 1
            k += 1

        while i < len(left):
            merged[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            merged[k] = right[j]
            j += 1
            k += 1

        return merged, inversions

    _, total_inversions = merge_and_count(nums)
    return total_inversions
print(count_inversions([8, 4, 2, 1]))  