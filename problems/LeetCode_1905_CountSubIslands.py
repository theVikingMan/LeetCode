def solution(grid1, grid2):
  ROWS, COLS = len(grid1), len(grid1[0])
  visit = set() #so we dont visit the same point again in grid 2

  def dfs(r, c):
    if (r < 0 or c < 0 or r == ROWS or c == COLS or grid2[r][c] == 0 or (r, c) in visit):
      return True # Base cases that we are in bounds. BUT not saying that its invalid, just end of current grid2 island

    res = True
    visit.add((r, c))

    if grid1[r][c] == 0: # the initial base case is not excuted if grid 2 is an island. This checke
      res = False

    # Checking if the current grid2 island is a subisland. Not too many 1s in grid2
    # All it takes is one missing cell in grid1 to return False
    res = dfs(r + 1, c) and res
    res = dfs(r - 1, c) and res
    res = dfs(r, c + 1) and res
    res = dfs(r, c - 1) and res

    return res

  count = 0
  for r in range(ROWS):
    for c in range(COLS):
      if grid2[r][c] and (r,c) not in visit and dfs(r, c): # Only want to run DFS on an island in grid 2 and not visited
        count += 1
  return count


print(solution([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]])) #output: 3