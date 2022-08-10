
# ----------- BFS w/ Queue (valid) ----------- #

import collections

def ladderLength(beginWord, endWord, wordList):
  if endWord not in wordList:
    return 0

  if beginWord not in wordList:
    wordList.append(beginWord)

  graph = collections.defaultdict(list)
  for w in wordList:
    for j in range(len(w)):
      pattern = w[:j] + '*' + w[j+1:]
      graph[pattern].append(w)

  visit = set([beginWord]) # [] means you can add to the set without it breaking up
  q = collections.deque([beginWord])
  level = 1

  while q:
    for _ in range(len(q)):
      word = q.popleft()
      if word == endWord:
        return level
      for j in range(len(word)):
        pattern = word[:j] + '*' + word[j+1:]
        for nei in graph[pattern]:
          if nei not in visit:
            visit.add(nei)
            q.append(nei)
    level += 1
  return 0

print(ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))


# ---------- DFS (not fast enough) ------ #

# def ladderLength(beginWord, endWord, wordList):
#   if endWord not in wordList:
#     return 0

#   result = float('inf')
#   graph = collections.defaultdict(list)
#   if beginWord not in wordList:
#     wordList.append(beginWord)

#   for i in range(len(wordList) - 1):
#     for j in range(i + 1, len(wordList)):
#       first_word, second_word = wordList[i], wordList[j]
#       if compare(first_word, second_word):
#         graph[first_word].append(second_word)
#         graph[second_word].append(first_word)

#   visit = {}
#   def dfs(current_word):
#     if current_word == endWord:
#       return 1
#     if current_word in visit and visit[current_word] == -1:
#       return visit[current_word]

#     visit[current_word] = -1
#     steps = float('inf')

#     for nei in graph[current_word]:
#       outcome = dfs(nei)
#       if outcome != -1:
#         steps = min(steps, 1 + outcome)

#     visit[current_word] = steps
#     return steps
#   result = dfs(beginWord)
#   return result if result != float('inf') else 0


# def compare(word1, word2):
#   # if abs(len(word1) - len(word2)) > 1:
#   #   return False
#   one, two = 0, 0
#   diff = 0
#   while one < len(word1) and two < len(word2):
#     if word1[one] != word2[two]:
#       diff += 1
#     one += 1
#     two += 1
#   return diff < 2