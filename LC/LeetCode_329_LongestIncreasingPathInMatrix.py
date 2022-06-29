def solution(matrix):
  ROWS, COLS = len(matrix), len(matrix[0])
  dp = {}
  res = 0
  visit = set()


  def dfs(r, c, prev):
    if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or matrix[r][c] >= prev:
      return 0
    if (r, c) in dp:
      return dp[(r, c)]

    visit.add((r,c))
    dp[(r, c)] = 1 + max(dfs(r + 1, c, matrix[r][c]),
                          dfs(r, c + 1, matrix[r][c]),
                          dfs(r - 1, c, matrix[r][c]),
                          dfs(r, c - 1, matrix[r][c]))
    visit.remove((r,c))
    return dp[(r,c)]

  for r in range(ROWS):
    for c in range(COLS):
      res = max(res, dfs(r, c, float('inf')))
  return res

print(solution([[9,9,4],[6,6,8],[2,1,1]]))