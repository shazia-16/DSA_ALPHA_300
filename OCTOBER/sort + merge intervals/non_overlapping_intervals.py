def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0

    # Sort by end time to greedily keep intervals that end earliest
    intervals.sort(key=lambda x: x[1])

    removals = 0
    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):
        # Overlap occurs if current start < previous end
        if intervals[i][0] < prev_end:
            removals += 1  # Remove current interval
        else:
            prev_end = intervals[i][1]  # Update previous end time

    return removals
print(eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])) 