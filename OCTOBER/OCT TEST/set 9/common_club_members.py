m, n = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

seen = set()
common = []

for x in A:
    seen.add(x)

for x in B:
    if x in seen:
        common.append(x)
        seen.remove(x)

def merge_sort(a):

    if len(a) <= 1:
        return a

    mid = len(a) // 2

    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

common = merge_sort(common)

if len(common) == 0:
    print("None")
else:
    print(*common)