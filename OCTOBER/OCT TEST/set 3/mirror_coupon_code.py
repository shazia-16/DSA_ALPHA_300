s = input()

left = 0
right = len(s) - 1
flag = True

while left < right:

    while left < right and not s[left].isalnum():
        left += 1

    while left < right and not s[right].isalnum():
        right -= 1

    if s[left].lower() != s[right].lower():
        flag = False
        break

    left += 1
    right -= 1

if flag:
    print("YES")
else:
    print("NO")