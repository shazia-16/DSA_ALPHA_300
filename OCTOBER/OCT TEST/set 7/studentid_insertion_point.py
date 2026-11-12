n = int(input())
a = list(map(int, input().split()))
t = int(input())

low = 0
high = n

while low < high:

    mid = low + (high - low) // 2

    if a[mid] < t:
        low = mid + 1
    else:
        high = mid

print(low)