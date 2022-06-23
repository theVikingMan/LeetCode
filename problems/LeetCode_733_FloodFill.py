def floodFill(image, sr, sc, color):
  visit = set()
  ROWS, COLS = len(image), len(image[0])
  startColor = image[sr][sc]

  def dfs(r, c):
    if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or image[r][c] != startColor:
      return

    visit.add((r,c))
    image[r][c] = color

    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)

  dfs(sr, sc)
  return image

print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))