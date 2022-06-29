def longestStrChain(words):
    words.sort(key=lambda word: len(word))
    d = {word: 1 for word in words}
    answer = 1 # Impossible to have a sequence of length 0.

    for word in words:
        for i in range(len(word)):
            prev = word[:i] + word[i+1:]
            if prev in d:
                d[word] = max(1 + d[prev], d[word])
                answer = max(answer, d[word])

    return answer

print(longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))



# --------------- Using a Graph --------------- #

# from collections import defaultdict

# def longestStrChain(words):
#   graph = defaultdict(set)
#   words = set(words)

#   for word in words:
#       if len(word) > 1: # one-letter words have no predecessors
#           for i in range(len(word)):
#               prev = word[:i] + word[i+1:]
#               if prev in words:
#                   graph[prev].add(word)

#   def dfs(word):
#       # if the word has no neighbors, it is a sequence of a length 1, and we can never have a sequence of length 0.
#       answer = 1
#       for nei in graph[word]:
#           answer = max(answer, 1 + dfs(nei))
#       return answer
#   return max(dfs(word) for word in words)