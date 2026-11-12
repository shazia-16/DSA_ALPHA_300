s = input()
p = input()

n = len(s)
m = len(p)

if m > n:
    print("None")
else:
    a = [0] * 26
    b = [0] * 26

    for i in range(m):
        a[ord(s[i]) - 97] += 1
        b[ord(p[i]) - 97] += 1

    ans = []

    if a == b:
        ans.append(0)

    for i in range(m, n):
        a[ord(s[i - m]) - 97] -= 1
        a[ord(s[i]) - 97] += 1

        if a == b:
            ans.append(i - m + 1)

    if len(ans) == 0:
        print("None")
    else:
        print(*ans)