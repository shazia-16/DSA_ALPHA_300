def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    lo = 0
    hi = m * n - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        # Map 1D mid index to 2D matrix coordinates (row, col)
        row = mid // n
        col = mid % n
        val = matrix[row][col]

        if val == target:
            return True
        elif val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
mat = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
int(searchMatrix(mat, 3)) 