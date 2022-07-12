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

# --------------- Recursion w/ Memo ------------ #

# def longestStrChain(words):
#   words.sort(key=lambda i:len(i))
#   setWords = set(words)
#   dp = {}
#   res = 1

#   def helper(string):
#     if len(string) == 1:
#       return 1
#     if string in dp:
#       return dp[string]

#     outcome = 1
#     for j in range(len(string)):
#       prev = string[:j] + string[j+1:]
#       if prev in setWords:
#         outcome = max(outcome, 1 + helper(prev))
#     dp[string] = outcome
#     return dp[string]

#   for i in range(len(words) -1, -1, -1):
#     res = max(res, helper(words[i]))
#   return res