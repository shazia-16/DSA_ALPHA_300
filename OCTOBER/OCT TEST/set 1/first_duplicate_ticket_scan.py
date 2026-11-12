n = int(input())
a = list(map(int, input().split()))

seen = set()
ans = -1

for x in a:
    if x in seen:
        ans = x
        break
    seen.add(x)

print(ans)