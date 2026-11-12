n = int(input())
a = list(map(int, input().split()))
T = int(input())

d = {}

for i in range(n):
    x = T - a[i]

    if x in d:
        print(d[x], i)
        break

    d[a[i]] = i