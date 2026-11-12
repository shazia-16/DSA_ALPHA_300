n = int(input())

a = []

for i in range(n):
    s, e = map(int, input().split())
    a.append((s, e))

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

        if left[i][0] <= right[j][0]:
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

a = merge_sort(a)

result = []

start, end = a[0]

for i in range(1, n):

    s, e = a[i]

    if s <= end:
        if e > end:
            end = e
    else:
        result.append((start, end))
        start = s
        end = e

result.append((start, end))

for s, e in result:
    print(s, e)