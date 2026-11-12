n = int(input())
a = list(map(int, input().split()))

passes = 0

for i in range(n - 1):
    swapped = False

    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swapped = True

    if swapped:
        passes += 1
    else:
        break

print(*a)
print(passes)