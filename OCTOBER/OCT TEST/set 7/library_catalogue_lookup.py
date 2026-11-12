n = int(input())
a = list(map(int, input().split()))
q = int(input())

low = 0
high = n - 1
ans = -1

while low <= high:

    mid = low + (high - low) // 2

    if a[mid] == q:
        ans = mid
        break

    elif a[mid] < q:
        low = mid + 1

    else:
        high = mid - 1

print(ans)