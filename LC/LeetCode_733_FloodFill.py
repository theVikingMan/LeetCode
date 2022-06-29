import collections
# --------------- Recursive approach with visit set --------------- #

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

# --------------- Iterative with Queue --------------- #

def floodFill(image, sr, sc, color):
  visit = set()
  ROWS, COLS = len(image), len(image[0])
  startColor = image[sr][sc]
  q = collections.deque([[sr, sc]])

  while q:
    r, c = q.popleft()
    image[r][c] = color
    visit.add((r,c))

    directions = [[0,1], [0,-1], [1,0], [-1,0]]
    for rExtra, cExtra in directions:
      rx, cy = r + rExtra, c + cExtra
      if rx >= 0 and cy >= 0 and rx < ROWS and cy < COLS and image[rx][cy] == startColor and (rx,cy) not in visit:
        q.append([rx, cy])
  return image