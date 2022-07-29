def allPathsSourceTarget(graph):
  n = len(graph)
  g = { i:[] for i in range(n) }

  for i in range(n):
    for p in graph[i]:
      g[i].append(p)


  dp = {}
  def dfs(node):
    if node in dp:
      return dp[node]
    if node == n - 1:
      return [[node]]
    res = []
    for nei in g[node]:
      for path in dfs(nei):
        res.append([node] + path)

    dp[node] = res
    return dp[node]

  return dfs(0)

print(allPathsSourceTarget([[1,2],[3],[3],[]]))