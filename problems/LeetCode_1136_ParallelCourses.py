def minimumSemesters(n, relations):
  adj = { i:[] for i in range(1, n+1) }
  for pre, aft in relations:
    adj[aft].append(pre)

  visit = {}
  res = 0

  def dfs(val):
    if val in visit:
      return visit[val]
    visit[val] = -1
    maxLength = 1
    for pre in adj[val]:
      length = dfs(pre)
      if length == -1:
        return -1
      maxLength = max(length+1, maxLength)
    visit[val] = maxLength
    return maxLength

  for i in range(1, n+1):
    if adj[i]:
      outcome = dfs(i)
      if outcome == -1:
        return -1
      res = max(res, outcome)

  return res

print(minimumSemesters(3, [[1,3],[2,3]]))