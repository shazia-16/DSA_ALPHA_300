n = int(input())
a = list(map(int, input().split()))
T = int(input())

left = 0
right = n - 1

while left < right:

    total = a[left] + a[right]

    if total == T:
        print(left + 1, right + 1)
        break

    elif total < T:
        left += 1
    else:
        right -= 1