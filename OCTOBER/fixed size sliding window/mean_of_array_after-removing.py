def my_merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left_half = []
    for i in range(mid):
        left_half.append(arr[i])
        
    right_half = []
    for i in range(mid, len(arr)):
        right_half.append(arr[i])
        
    left_sorted = my_merge_sort(left_half)
    right_sorted = my_merge_sort(right_half)
    
    merged = []
    i = 0
    j = 0
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        else:
            merged.append(right_sorted[j])
            j += 1
            
    while i < len(left_sorted):
        merged.append(left_sorted[i])
        i += 1
    while j < len(right_sorted):
        merged.append(right_sorted[j])
        j += 1
        
    return merged

def trim_mean(arr: list[int]) -> float:
    sorted_arr = my_merge_sort(arr)
    n = len(sorted_arr)
    trim = n // 20  # 5% from each end
    
    total = 0
    count = 0
    for i in range(trim, n - trim):
        total += sorted_arr[i]
        count += 1
        
    return total / count