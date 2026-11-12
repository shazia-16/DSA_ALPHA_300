n, k, T = map(int, input().split())
a = list(map(int, input().split()))

total = 0
count = 0

for i in range(k):
    total += a[i]

if total >= k * T:
    count += 1

for i in range(k, n):
    total = total - a[i - k] + a[i]

    if total >= k * T:
        count += 1

print(count)