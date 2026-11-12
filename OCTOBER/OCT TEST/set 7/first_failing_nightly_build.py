n = int(input())
a = list(map(int, input().split()))

low = 0
high = n - 1
ans = -1

while low <= high:

    mid = low + (high - low) // 2

    if a[mid] == 1:
        ans = mid + 1
        high = mid - 1

    else:
        low = mid + 1

print(ans)