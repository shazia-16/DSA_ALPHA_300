n = int(input())
a = list(map(int, input().split()))

pos = 0

for i in range(n):
    if a[i] != 0:
        a[pos] = a[i]
        pos += 1

while pos < n:
    a[pos] = 0
    pos += 1

print(*a)