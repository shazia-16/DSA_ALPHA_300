n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    x = abs(a[i])
    index = x - 1

    if a[index] > 0:
        a[index] = -a[index]

missing = []

for i in range(n):
    if a[i] > 0:
        missing.append(i + 1)

if len(missing) == 0:
    print("None")
else:
    print(*missing)