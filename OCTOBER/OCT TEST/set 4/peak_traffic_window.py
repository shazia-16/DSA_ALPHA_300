n, k = map(int, input().split())
a = list(map(int, input().split()))

total = 0

for i in range(k):
    total += a[i]

maximum = total

for i in range(k, n):
    total = total - a[i - k] + a[i]

    if total > maximum:
        maximum = total

print(maximum)