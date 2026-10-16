def frequency_sort(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    unique_chars = list(counts.keys())          #extract unique characters with list
    n = len(unique_chars)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if counts[unique_chars[j]] > counts[unique_chars[max_idx]]:
                max_idx = j
        unique_chars[i], unique_chars[max_idx] = (          #swap character keys
            unique_chars[max_idx],
            unique_chars[i],
        )
    result_chars = [None] * len(s)
    pos = 0
    for char in unique_chars:
        freq = counts[char]
        for _ in range(freq):
            result_chars[pos] = char
            pos += 1
    return "".join(result_chars)
print(frequency_sort("tree"))