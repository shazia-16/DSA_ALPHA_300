def frequencySort(nums: list[int]) -> list[int]:
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    def is_less_than(a: int, b: int) -> bool:
        if freq[a] != freq[b]:
            return freq[a] < freq[b]
        return a > b  # Larger value comes first if frequencies are equal

    def merge_sort(arr: list[int]) -> list[int]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        sorted_arr = []
        i = j = 0
        while i < len(left) and j < len(right):
            if is_less_than(left[i], right[j]):
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        return sorted_arr
    return merge_sort(nums)
print(frequencySort([1, 1, 2, 2, 2, 3]))  