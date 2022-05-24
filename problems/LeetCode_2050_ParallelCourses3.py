
def minimumTime(n, relations, time):
  # STEP 1: Create adjceny list
  adj = { i:[] for i in range(1, n + 1) }
  for pre, after in relations:
    adj[after].append(pre)

  visit = {}
  res = 0

  # STEP 2: DFS down evey node and its children
  def dfs(node):
    if node in visit:
      return visit[node] # if we have already looked at a nodes path, return max time for that path
    visit[node] = -1 # mark as visited currently in this particular cycle
    t = time[node - 1] # curr time is the curr node's time
    for pre in adj[node]: # traverse every childe to get the max time for each child's DFS path
      otherTime = dfs(pre) # return value will be time for each child
      if t == -1: # if we have already seen it in the cycle, return -1 that means invalid answer
        return -1
      t = max(t, otherTime + time[node - 1]) # after each child, update the max for that child's path + parent time or a prior combination's max
    visit[node] = t # store max value. Usually changed to False to indicate that we have already analyzed it but now its not in the cycle
    return t # return the output back up

  # STEP 3: Run DFS and update for new maxes returned
  for i in range(1, n + 1): # need to check every i. What is there is only one i and it has no children, that would return 0
    t = dfs(i)
    if t == -1:
      return -1
    res = max(t, res) # max of each path
  return res

print(minimumTime(1,[],[1]))
# print(minimumTime(5, [[1,5],[2,5],[3,5],[3,4],[4,5]], [1,2,3,4,5]))