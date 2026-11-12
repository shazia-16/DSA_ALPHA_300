n, k = map(int, input().split())
a = list(map(int, input().split()))

target = n - k
left = 0
right = n - 1

while left <= right:

    pivot = a[right]
    i = left

    for j in range(left, right):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1

    a[i], a[right] = a[right], a[i]

    if i == target:
        print(a[i])
        break
    elif i < target:
        left = i + 1
    else:
        right = i - 1