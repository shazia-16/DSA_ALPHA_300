n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(k):
    smallest = i

    for j in range(i + 1, n):
        if a[j] < a[smallest]:
            smallest = j

    a[i], a[smallest] = a[smallest], a[i]

print(*a[:k])