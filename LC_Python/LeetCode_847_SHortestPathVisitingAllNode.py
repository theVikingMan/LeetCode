import collections

def shortestPathLength(graph):
  n = len(graph)
  adjList = { i:collections.deque() for i in range(n) }
  for i, arr in enumerate(graph):
    for child in arr:
      adjList[i].append(child)

  seen = []
  def dfs(node):
    if len(set(seen)) == n:
      return 0
    if node not in adjList:
      return float('inf')

    outcome = float('inf')
    temp = list(adjList[node])

    for nei in temp:
      adjList[node].popleft()
      seen.append(nei)
      outcome = min(outcome, 1 + dfs(nei))
      adjList[node].append(nei)
      seen.pop()
    return outcome

  result = [float('inf')]
  for i in range(n):
    seen.append(i)
    result[0] = min(result[0], dfs(i))
    seen.pop()
  return result[0]

print(shortestPathLength([[1,2,3],[0],[0],[0]]))