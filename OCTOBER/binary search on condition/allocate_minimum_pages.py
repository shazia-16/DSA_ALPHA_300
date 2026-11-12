def findPages(arr: list[int], k: int) -> int:
    # If students exceed the number of books, allocation is impossible
    if k > len(arr):
        return -1
    lo = max(arr)
    hi = sum(arr)
    ans = -1

    # Feasibility check: Can we allocate books such that no student gets > max_pages?
    def is_possible(max_pages: int) -> bool:
        students = 1
        current_pages = 0
        for pages in arr:
            if current_pages + pages > max_pages:
                students += 1
                current_pages = pages
            else:
                current_pages += pages
        return students <= k
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if is_possible(mid):
            ans = mid
            hi = mid - 1  # Feasible -> try minimizing max pages further
        else:
            lo = mid + 1  # Infeasible -> increase page limit
    return ans
print(findPages([12, 34, 67, 90], 2)) 