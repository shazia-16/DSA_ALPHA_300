n, t = map(int, input().split())
a = list(map(int, input().split()))

count = [0] * 101

for x in a:
    count[x] += 1

total = 0
position = 0

for i in range(101):

    for j in range(count[i]):

        if position >= t and position < n - t:
            total += i

        position += 1

remaining = n - 2 * t

mean = total / remaining

print("%.2f" % mean)