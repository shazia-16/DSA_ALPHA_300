n = int(input())

a = []

for i in range(n):
    s, e = map(int, input().split())
    a.append((s, e))

new_s, new_e = map(int, input().split())

result = []
i = 0

while i < n and a[i][1] < new_s:
    result.append(a[i])
    i += 1

while i < n and a[i][0] <= new_e:

    if a[i][0] < new_s:
        new_s = a[i][0]

    if a[i][1] > new_e:
        new_e = a[i][1]

    i += 1

result.append((new_s, new_e))

while i < n:
    result.append(a[i])
    i += 1

for s, e in result:
    print(s, e)