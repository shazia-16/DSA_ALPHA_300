def merge_two_sorted_arrays(nums1, nums2):
    len1, len2 = len(nums1), len(nums2)
    merged = [None] * (len1 + len2)
    i = 0
    j = 0
    k = 0

    while i < len1 and j < len2:
        if nums1[i] <= nums2[j]:
            merged[k] = nums1[i]
            i += 1
        else:
            merged[k] = nums2[j]
            j += 1
        k += 1

    while i < len1:
        merged[k] = nums1[i]
        i += 1
        k += 1

    while j < len2:
        merged[k] = nums2[j]
        j += 1
        k += 1

    return merged
print( merge_two_sorted_arrays([1, 3, 5, 7], [2, 4, 6, 8])) 