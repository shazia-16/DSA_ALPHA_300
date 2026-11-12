n = int(input())
a = list(map(int, input().split()))

first = None
second = None

for x in a:
    if first is None or x > first:
        if x != first:
            second = first
            first = x
    elif x != first:
        if second is None or x > second:
            second = x

if second is None:
    print("None")
else:
    print(second)