import collections
from lib2to3.pgen2.literals import evalString

def calcEquation(equations, values, queries):
  graph = collections.defaultdict(dict)
  for eq, val in zip(equations, values):
    first, second = eq[0], eq[1]
    graph[first][second] = val
    graph[second][first] = 1 / val


  def dfs(firstL, secondL, pro):
    visited.add(firstL)
    res = -1
    nei = graph[firstL]
    if secondL in nei:
      res = pro * nei[secondL]
    else:
      for neighbor, value in nei.items():
        if neighbor not in visited:
          res = dfs(neighbor, secondL, pro * value)
        if res != -1:
          break
    visited.remove(firstL)
    return res


  result = []
  visited = set()

  for one, two in queries:
    if one not in graph or two not in graph:
      result.append(float(-1))
    elif one == two:
      result.append(float(1))
    else:
      result.append(dfs(one, two, 1))
  return result

print(calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],
[3.0,4.0,5.0,6.0],
[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]))