n = int(input())
a = list(map(int, input().split()))

freq = {}

for x in a:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

ans = -1

for x in a:
    if freq[x] == 1:
        ans = x
        break

print(ans)