R, C = map(int, input().split())

a = []

for i in range(R):
    row = list(map(int, input().split()))
    a.append(row)

t = int(input())

low = 0
high = R * C - 1
ans = -1

while low <= high:

    mid = (low + high) // 2

    r = mid // C
    c = mid % C

    if a[r][c] == t:
        ans = mid
        break

    elif a[r][c] < t:
        low = mid + 1
    else:
        high = mid - 1

if ans == -1:
    print(-1, -1)
else:
    print(ans // C, ans % C)