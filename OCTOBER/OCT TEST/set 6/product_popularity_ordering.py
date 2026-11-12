n = int(input())
a = list(map(int, input().split()))

freq = {}

for x in a:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

items = []

for x in freq:
    items.append((freq[x], x))

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

        if left[i][0] < right[j][0]:
            result.append(left[i])
            i += 1

        elif left[i][0] > right[j][0]:
            result.append(right[j])
            j += 1

        elif left[i][1] > right[j][1]:
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

items = merge_sort(items)

ans = []

for f, x in items:
    for j in range(f):
        ans.append(x)

print(*ans)