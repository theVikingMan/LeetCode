def solution(edges):
  parents = [i for i in range(len(edges) + 1)]
  rank = [1 for _ in range(len(edges) + 1)]

  def find(val):
    res = val
    while res != parents[res]:
      parents[res] = parents[parents[res]]
      res = parents[res]
    return res

  def union(n1, n2):
    par1, par2 = find(n1), find(n2)
    if par1 == par2:
      return False
    if rank[par1] > rank[par2]:
      parents[par2] = par1
      rank[par1] += rank[par2]
    else:
      parents[par1] = par2
      rank[par2] += rank[par1]
    return True

  for n1, n2 in edges:
    if not union(n1, n2):
      return [n1, n2]

print(solution([[1,2],[1,3],[2,3]]))