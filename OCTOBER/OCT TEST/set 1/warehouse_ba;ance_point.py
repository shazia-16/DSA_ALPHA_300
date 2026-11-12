n = int(input())
a = list(map(int, input().split()))

total = 0

for x in a:
    total += x

left = 0
ans = -1

for i in range(n):
    right = total - left - a[i]

    if left == right:
        ans = i
        break

    left += a[i]

print(ans)