def rowWithMax1s(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return -1
    m, n = len(matrix), len(matrix[0])
    max_ones = 0
    row_idx = -1
    # Custom helper to find first occurrence of 1 in a sorted row
    def find_first_one(row: list[int]) -> int:
        lo, hi = 0, len(row) - 1
        first_one = len(row)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if row[mid] == 1:
                first_one = mid
                hi = mid - 1  # Search left side for earlier 1s
            else:
                lo = mid + 1
        return first_one
    for r in range(m):
        first_one_pos = find_first_one(matrix[r])
        ones_count = n - first_one_pos
        
        if ones_count > max_ones:
            max_ones = ones_count
            row_idx = r
    return row_idx
mat = [
   [0, 1, 1, 1],
   [0, 0, 1, 1],
   [1, 1, 1, 1],
   [0, 0, 0, 0]
]
print(rowWithMax1s(mat))