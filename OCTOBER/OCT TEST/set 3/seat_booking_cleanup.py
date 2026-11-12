n = int(input())
a = list(map(int, input().split()))

if n <= 2:
    k = n
else:
    k = 2

    for i in range(2, n):
        if a[i] != a[k - 2]:
            a[k] = a[i]
            k += 1

print(k)
print(*a[:k])