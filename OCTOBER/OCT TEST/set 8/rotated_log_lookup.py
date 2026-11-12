n = int(input())
a = list(map(int, input().split()))
t = int(input())

low = 0
high = n - 1
ans = -1

while low <= high:

    mid = (low + high) // 2

    if a[mid] == t:
        ans = mid
        break

    if a[low] <= a[mid]:

        if a[low] <= t < a[mid]:
            high = mid - 1
        else:
            low = mid + 1

    else:

        if a[mid] < t <= a[high]:
            low = mid + 1
        else:
            high = mid - 1

print(ans)