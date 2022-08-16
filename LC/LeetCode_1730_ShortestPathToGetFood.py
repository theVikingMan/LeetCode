import collections

def getFood(grid):
  ROWS, COLS = len(grid), len(grid[0])
  visit = set()

  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] == '*': # start traversal from starting point
        q = collections.deque([(0, r, c)]) # step, (position)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit.add((r, c))

        while q:
          steps, r, c = q.popleft()

          for rDir, cDir in directions:
            newR, newC = r + rDir, c + cDir
            if (0 <= newR < ROWS) and (0 <= newC < COLS) and grid[newR][newC] != 'X' and (newR, newC) not in visit:
              if grid[newR][newC] == '#':
                return steps + 1
              visit.add((newR, newC))
              q.append((steps + 1, newR, newC))

  return -1

print(getFood([["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]))


# def getFood(grid):
#   ROWS, COLS = len(grid), len(grid[0])
#   visit = set()

#   def bfs(r, c, steps):
#     if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == 'X':
#       return float('inf')

#     if grid[r][c] == '#':
#       return steps

#     visit.add((r, c))
#     res = min(bfs(r + 1, c, steps + 1),
#               bfs(r, c + 1, steps + 1),
#               bfs(r - 1, c, steps + 1),
#               bfs(r, c - 1, steps + 1))
#     visit.remove((r, c))

#     return res

#   for r in range(ROWS):
#     for c in range(COLS):
#       if grid[r][c] == '*':
#         result = bfs(r, c, 0)
#         return result if result != float('inf') else -1