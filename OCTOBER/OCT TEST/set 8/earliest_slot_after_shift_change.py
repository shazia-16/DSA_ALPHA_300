n = int(input())
a = list(map(int, input().split()))

low = 0
high = n - 1

while low < high:

    mid = (low + high) // 2

    if a[mid] > a[high]:
        low = mid + 1
    else:
        high = mid

print(a[low])