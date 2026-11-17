def sum_prefix_scores(words: list[str]) -> list[int]:
    trie = {}
    
    # Insert every word and count prefix occurrences
    for word in words:
        node = trie
        for ch in word:
            if ch not in node:
                node[ch] = {'count': 0}
            node = node[ch]
            node['count'] += 1
            
    # Calculate total prefix score for each word
    scores = []
    for word in words:
        node = trie
        score = 0
        for ch in word:
            node = node[ch]
            score += node['count']
        scores.append(score)
        
    return scores