n, k = map(int, input().split())
a = list(map(int, input().split()))

seen = set()
flag = False

for i in range(n):

    if a[i] in seen:
        flag = True
        break

    seen.add(a[i])

    if i >= k:
        seen.remove(a[i - k])

if flag:
    print("YES")
else:
    print("NO")