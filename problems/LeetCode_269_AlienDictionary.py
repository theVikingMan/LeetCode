def solution(words):
  adj = { c:set() for w in words for c in w } # list comp for getting all unique letters in words

  for i in range(len(words) - 1): # Looking at all pairs
    w1, w2 = words[i], words[i + 1] # Look at a pair
    minLen = min(len(w1), len(w2)) # base case testing if the pair is invalid
    if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: # Same prefix but ordering is wrong
      return ""
    for j in range(minLen):
      if w1[j] != w2[j]: # find the first letters that do not match
        adj[w1[j]].add(w2[j]) # add the letter that comes after w1 letter to the adj list
        break

  visit = {}
  res = []

  def dfs(c):
    if c in visit: # if we have seen it before
      return visit[c] # return if it is in the same cycle
    visit[c] = True # mark as the cycle
    for nei in adj[c]:
      if dfs(nei): # if the dfs of its neis says its been seen in this cycle
        return True # kill the algo
    visit[c] = False # No cycle detected? Say its not part of the same cycle
    res.append(c) # valid char, add it to res

  for c in adj:
    if dfs(c):
      return ""
  res.reverse()
  return "".join(res)

# print(solution(["z","x","z"]))
print(solution(["wrt","wrf","er","ett","rftt"]))