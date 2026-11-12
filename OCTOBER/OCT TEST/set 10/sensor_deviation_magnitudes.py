n = int(input())
a = list(map(int, input().split()))

result = [0] * n

left = 0
right = n - 1
pos = n - 1

while left <= right:

    x = a[left] * a[left]
    y = a[right] * a[right]

    if x > y:
        result[pos] = x
        left += 1
    else:
        result[pos] = y
        right -= 1

    pos -= 1

print(*result)