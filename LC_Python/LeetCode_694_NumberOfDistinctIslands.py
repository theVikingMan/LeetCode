def numDistinctIslands(grid):
  shapes = set()
  seen = set()
  res = 0
  ROWS, COLS = len(grid), len(grid[0])

  def dfs(r, c, rowOrigin, colOrigin):
    if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in seen or grid[r][c] == 0:
      return

    seen.add((r, c))
    currentIsland.add((r - rowOrigin, c - colOrigin))

    dfs(r, c - 1, rowOrigin, colOrigin)
    dfs(r, c + 1, rowOrigin, colOrigin)
    dfs(r + 1, c, rowOrigin, colOrigin)
    dfs(r - 1, c, rowOrigin, colOrigin)


  for r in range(ROWS):
    for c in range(COLS):
      if (r,c) not in seen and grid[r][c] == 1:
        currentIsland = set()
        dfs(r, c, r, c)
        if currentIsland not in shapes:
          res += 1
          shapes.add(frozenset(currentIsland))
  return res

print(numDistinctIslands([[0,0,1],[1,0,1],[1,1,0]]))