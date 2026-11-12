m, n = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i = 0
j = 0
result = []

while i < m and j < n:

    if A[i] < B[j]:
        x = A[i]
        i += 1
    elif A[i] > B[j]:
        x = B[j]
        j += 1
    else:
        x = A[i]
        i += 1
        j += 1

    if len(result) == 0 or result[-1] != x:
        result.append(x)

while i < m:
    if len(result) == 0 or result[-1] != A[i]:
        result.append(A[i])
    i += 1

while j < n:
    if len(result) == 0 or result[-1] != B[j]:
        result.append(B[j])
    j += 1

print(*result)