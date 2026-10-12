def total_fruit(fruits):
    n = len(fruits)
    left = 0
    max_fruits = 0
    basket = {}
    for right in range(n):
        fruit = fruits[right]
        if fruit in basket:
            basket[fruit] += 1
        else:
            basket[fruit] = 1
        while len(basket) > 2:
            left_fruit = fruits[left]
            basket[left_fruit] -= 1
            if basket[left_fruit] == 0:
                del basket[left_fruit]
            left += 1
        window_len = right - left + 1
        if window_len > max_fruits:
            max_fruits = window_len
    return max_fruits
print(total_fruit([1, 2, 1]))  