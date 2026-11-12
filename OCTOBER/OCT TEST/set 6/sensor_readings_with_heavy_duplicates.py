n = int(input())
a = list(map(int, input().split()))

stack = [(0, n - 1)]

while stack:

    low, high = stack.pop()

    if low >= high:
        continue

    mid = low + (high - low) // 2
    pivot = a[mid]

    lt = low
    i = low
    gt = high

    while i <= gt:

        if a[i] < pivot:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1

        elif a[i] > pivot:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1

        else:
            i += 1

    if low < lt - 1:
        stack.append((low, lt - 1))

    if gt + 1 < high:
        stack.append((gt + 1, high))

print(*a)