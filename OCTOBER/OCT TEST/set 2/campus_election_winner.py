n = int(input())
a = list(map(int, input().split()))

candidate = None
count = 0

for x in a:
    if count == 0:
        candidate = x

    if x == candidate:
        count += 1
    else:
        count -= 1

print(candidate)