n, k = map(int, input().split())
a = list(map(int, input().split()))

k = k % n

def reverse(a, left, right):
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1

reverse(a, 0, n - 1)
reverse(a, 0, k - 1)
reverse(a, k, n - 1)

print(*a)