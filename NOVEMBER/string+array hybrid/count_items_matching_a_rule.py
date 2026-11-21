def count_matches(items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
    if ruleKey == "type":
        idx = 0
    elif ruleKey == "color":
        idx = 1
    else:
        idx = 2

    matches = 0
    for item in items:
        if item[idx] == ruleValue:
            matches += 1

    return matches