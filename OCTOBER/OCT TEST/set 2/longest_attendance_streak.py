n, T = map(int, input().split())
a = list(map(int, input().split()))

count = 0
maximum = 0

for x in a:
    if x >= T:
        count += 1
    else:
        count = 0

    if count > maximum:
        maximum = count

print(maximum)