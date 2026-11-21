def buddy_strings(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False

    if s == goal:
        seen = set()
        for ch in s:
            if ch in seen:
                return True
            seen.add(ch)
        return False

    diffs = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            diffs.append(i)
            if len(diffs) > 2:
                return False

    if len(diffs) != 2:
        return False

    i = diffs[0]
    j = diffs[1]
    return s[i] == goal[j] and s[j] == goal[i]