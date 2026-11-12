n = int(input())
a = list(map(int, input().split()))
q = int(input())

# Find floor
low = 0
high = n - 1
floor = None

while low <= high:

    mid = (low + high) // 2

    if a[mid] <= q:
        floor = a[mid]
        low = mid + 1
    else:
        high = mid - 1

# Find ceiling
low = 0
high = n - 1
ceiling = None

while low <= high:

    mid = (low + high) // 2

    if a[mid] >= q:
        ceiling = a[mid]
        high = mid - 1
    else:
        low = mid + 1

print(floor, ceiling)