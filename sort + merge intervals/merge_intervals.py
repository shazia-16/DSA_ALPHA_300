def merge(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    # Sort intervals by their starting points
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged[-1]

        # Overlap condition: current start <= last merged end
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)

    return merged
print(merge([[1, 3], [2, 6], [8, 10], [15, 18]])) 