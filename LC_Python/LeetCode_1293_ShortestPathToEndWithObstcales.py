import collections

# ----------- Iterative / Faster ----------- #
def shortestPath(grid, k):
  ROWS, COLS = len(grid), len(grid[0])
  if k >= (ROWS + COLS - 2):
    return ROWS + COLS - 2

  target = (ROWS - 1, COLS - 1)
  q = collections.deque([(0, (0, 0, k))]) # step, (state)
  directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  seen = set([(0, 0, k)])

  while q:
    steps, (r, c, removals_left) = q.popleft()
    if (r, c) == target:
      return steps

    for rDir, cDir in directions:
      newR, newC = r + rDir, c + cDir

      if (0 <= newR < ROWS) and (0 <= newC < COLS):
        newRemovals = removals_left - grid[newR][newC]
        newState = (newR, newC, newRemovals)

        if newRemovals >= 0 and newState not in seen:
          seen.add(newState)
          q.append((steps + 1, newState))
  return -1

print(shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1))
# ----------- Recursive / Too Slow ----------- #

# def shortestPath(grid, k):
#   res = float('inf')
#   ROWS, COLS = len(grid), len(grid[0])
#   visit = set()

#   def dfs(r, c, k, steps):
#     nonlocal res
#     if r < 0 or c < 0 or r == ROWS or c == COLS or (grid[r][c] == 1 and k == 0) or (r,c) in visit or steps >= res:
#       return float('inf')
#     if r == ROWS - 1 and c == COLS - 1:
#       res = min(res, steps)

#     if grid[r][c] == 1: k -= 1
#     visit.add((r,c))

#     dfs(r + 1, c, k, steps + 1)
#     dfs(r, c + 1, k, steps + 1)
#     dfs(r, c - 1, k, steps + 1)
#     dfs(r - 1, c, k, steps + 1)

#     visit.remove((r,c))

#   dfs(0, 0, k, 0)
#   return res if res != float('inf') else -1