n = int(input())
a = list(map(int, input().split()))

low = 0
mid = 0
high = n - 1

while mid <= high:

    if a[mid] == 0:
        a[low], a[mid] = a[mid], a[low]
        low += 1
        mid += 1

    elif a[mid] == 1:
        mid += 1

    else:
        a[mid], a[high] = a[high], a[mid]
        high -= 1

print(*a)