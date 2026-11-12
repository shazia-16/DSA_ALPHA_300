n = int(input())
a = list(map(int, input().split()))
x = int(input())

low = 0
high = n - 1
first = -1

while low <= high:

    mid = (low + high) // 2

    if a[mid] == x:
        first = mid
        high = mid - 1

    elif a[mid] < x:
        low = mid + 1

    else:
        high = mid - 1

if first == -1:
    print(-1, -1)

else:
    low = first
    high = n - 1
    last = first

    while low <= high:

        mid = (low + high) // 2

        if a[mid] == x:
            last = mid
            low = mid + 1

        elif a[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    print(first, last)