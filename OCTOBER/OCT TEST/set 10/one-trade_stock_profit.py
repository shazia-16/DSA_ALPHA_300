n = int(input())
a = list(map(int, input().split()))

minimum = a[0]
profit = 0

for i in range(1, n):

    current = a[i] - minimum

    if current > profit:
        profit = current

    if a[i] < minimum:
        minimum = a[i]

print(profit)