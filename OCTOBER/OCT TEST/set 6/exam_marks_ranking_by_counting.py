n = int(input())
a = list(map(int, input().split()))

count = [0] * 101

for x in a:
    count[x] += 1

result = []

for i in range(101):
    for j in range(count[i]):
        result.append(i)

print(*result)