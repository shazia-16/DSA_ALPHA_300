n, q = map(int, input().split())
a = list(map(int, input().split()))

prefix = [0] * n
prefix[0] = a[0]

for i in range(1, n):
    prefix[i] = prefix[i - 1] + a[i]

for _ in range(q):
    l, r = map(int, input().split())

    if l == 0:
        print(prefix[r])
    else:
        print(prefix[r] - prefix[l - 1])