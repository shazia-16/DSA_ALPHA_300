n = int(input())
a = list(map(int, input().split()))

def merge_sort(a):
    if len(a) <= 1:
        return a, 0

    mid = len(a) // 2

    left, c1 = merge_sort(a[:mid])
    right, c2 = merge_sort(a[mid:])

    i = 0
    j = 0
    merged = []
    count = c1 + c2

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left) - i
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged, count

result, count = merge_sort(a)
print(count)