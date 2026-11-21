def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    seen = set()
    for num in nums1:
        seen.add(num)
        
    result = []
    added = set()
    for num in nums2:
        if num in seen and num not in added:
            result.append(num)
            added.add(num)
            
    return result