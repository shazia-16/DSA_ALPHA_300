def findPeakGrid(mat: list[list[int]]) -> list[int]:
    m, n = len(mat), len(mat[0])
    lo = 0
    hi = n - 1
    while lo <= hi:
        mid_col = lo + (hi - lo) // 2
        # 1. Find the row index of the maximum element in mid_col
        max_row = 0
        for r in range(m):
            if mat[r][mid_col] > mat[max_row][mid_col]:
                max_row = r
        # 2. Check left and right neighbors of mat[max_row][mid_col]
        left_val = mat[max_row][mid_col - 1] if mid_col - 1 >= 0 else -1
        right_val = mat[max_row][mid_col + 1] if mid_col + 1 < n else -1
        current_val = mat[max_row][mid_col]
        # 3. Peak condition
        if current_val > left_val and current_val > right_val:
            return [max_row, mid_col]
        # Slope is rising to the right
        elif right_val > current_val:
            lo = mid_col + 1
        # Slope is rising to the left
        else:
            hi = mid_col - 1
    return [-1, -1]
grid = [
   [10, 20, 15],
   [21, 30, 14],
   [ 7, 16, 32]
 ]
print(findPeakGrid(grid)) 