n, m = map(int, input().split())
a = list(map(int, input().split()))

if m > n:
    print(-1)

else:

    low = a[0]
    high = 0

    for x in a:

        if x > low:
            low = x

        high += x

    ans = high

    while low <= high:

        mid = (low + high) // 2

        groups = 1
        total = 0

        for x in a:

            if total + x <= mid:
                total += x

            else:
                groups += 1
                total = x

        if groups <= m:
            ans = mid
            high = mid - 1

        else:
            low = mid + 1

    print(ans)