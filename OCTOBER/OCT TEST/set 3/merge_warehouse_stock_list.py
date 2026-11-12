m, n = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i = m - 1
j = n - 1
k = m + n - 1

while i >= 0 and j >= 0:

    if A[i] > B[j]:
        A[k] = A[i]
        i -= 1
    else:
        A[k] = B[j]
        j -= 1

    k -= 1

while j >= 0:
    A[k] = B[j]
    j -= 1
    k -= 1

print(*A)