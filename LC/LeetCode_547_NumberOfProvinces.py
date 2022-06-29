def findCircleNum(isConnected):
  lenNodes = len(isConnected) # storing length result
  outcome = lenNodes # number how many nodes exist

  parents = [i for i in range(lenNodes + 1)]
  rank = [1 for _ in range(lenNodes + 1)]

  # create adj list (usually given in most problems)
  adj = { i:[] for i in range(lenNodes) }
  for i in range(lenNodes):
    for j in range(len(isConnected[i])):
      if j != i and isConnected[i][j] == 1:
        adj[i].append(j)

  def find(node):
    res = node
    while res != parents[res]:
      parents[res] = parents[parents[res]] # path compression
      res = parents[res] # move node up on family tree
    return res # reached parent

  def union(n1, n2):
    par1, par2 = find(n1), find(n2)
    if par1 == par2: # if already union'd
      return 0
    if rank[par1] > rank[par2]:
      parents[par2] = par1
      rank[par1] += rank[par2]
    else:
      parents[par1] = par2
      rank[par2] += rank[par1]
    return 1

  for i in range(lenNodes):
    for nei in adj[i]:
      outcome -= union(i, nei)

  return outcome

print(findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))