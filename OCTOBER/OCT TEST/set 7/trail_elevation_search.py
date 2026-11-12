n = int(input())
a = list(map(int, input().split()))
h = int(input())

low = 0
high = n - 1

while low < high:

    mid = (low + high) // 2

    if a[mid] < a[mid + 1]:
        low = mid + 1
    else:
        high = mid

peak = low

# Search increasing part
low = 0
high = peak
ans = -1

while low <= high:

    mid = (low + high) // 2

    if a[mid] == h:
        ans = mid
        break

    elif a[mid] < h:
        low = mid + 1
    else:
        high = mid - 1

# Search decreasing part if not found
if ans == -1:

    low = peak + 1
    high = n - 1

    while low <= high:

        mid = (low + high) // 2

        if a[mid] == h:
            ans = mid
            break

        elif a[mid] > h:
            low = mid + 1
        else:
            high = mid - 1

print(ans)