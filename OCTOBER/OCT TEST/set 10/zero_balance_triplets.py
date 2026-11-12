n = int(input())
a = list(map(int, input().split()))

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

a = merge_sort(a)

found = False

for i in range(n - 2):

    if i > 0 and a[i] == a[i - 1]:
        continue

    left = i + 1
    right = n - 1

    while left < right:

        total = a[i] + a[left] + a[right]

        if total == 0:

            print(a[i], a[left], a[right])
            found = True

            x = a[left]
            y = a[right]

            while left < right and a[left] == x:
                left += 1

            while left < right and a[right] == y:
                right -= 1

        elif total < 0:
            left += 1

        else:
            right -= 1

if not found:
    print("None")