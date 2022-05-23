def solution(equations):
  # iterator constructor for alphabet. Adj list for each letter as itself for the parent
  parents = {chr(num):chr(num) for num in range(ord("a"), ord("z")+1)}
  rank = [1] * 27 # ranking for more optimizagtion

  def find(val): # find root parents
    res = val
    while res != parents[res]: # base case: parent of itself
      parents[res] = parents[parents[res]] # path compression. Skipping to Grand parent if possible
      res = parents[res]
    return res

  def union(n1, n2): # Union nodes by making parents the same
    x, y = find(n1), find(n2) # find parents
    if x == y: # already union'd
      return
    if rank[ord(x) - 96] > rank[ord(y) - 96]: # adjust rankings and parents based on rankings
      parents[y] = x
      rank[ord(x) - 96] += 1
    else:
      parents[x] = y
      rank[ord(y) - 96] += 1


  for x,sign,_,y in equations: # deconstruct string into components
    if sign == "=": # letters should be equal
      union(x, y)

  for x,sign,_,y in equations: # if any not equal equations
    if sign == "!" and find(x) == find(y): # see if there is a mismatch
        return False

  return True

print(solution(["a==z","a==b","b==c","c==d","b==y","c==x","d==w","g==h","h==i","i==j","a==g","j!=y"])) # false