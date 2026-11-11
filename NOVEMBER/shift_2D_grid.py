def shift_grid_chars(grid: list[list[str]], k: int) -> list[list[str]]:
    rows = len(grid)
    if rows == 0:
        return grid
    cols = len(grid[0])
    total = rows * cols
    if total == 0:
        return grid

    # Normalize k to prevent unnecessary full rotations
    k = k % total

    # Initialize result grid with empty placeholders
    result = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append("")
        result.append(row)

    # Map linear index of rotated elements back to 2D grid coordinates
    for i in range(total):
        # Calculate new 1D index after shifting k positions
        new_i = (i + k) % total
        
        # Convert 1D indices back into 2D coordinates
        orig_r = i // cols
        orig_c = i % cols
        new_r = new_i // cols
        new_c = new_i % cols
        
        result[new_r][new_c] = grid[orig_r][orig_c]

    return result
grid = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
print(shift_grid_chars(grid, 1))