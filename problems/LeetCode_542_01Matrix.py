import collections

def updateMatrix(mat):
  ROWS, COLS = len(mat), len(mat[0])
  res = [[0 for _ in range(COLS)] for _ in range(ROWS)]
  visit = {}

  q = collections.deque()

  for r in range(ROWS):
    for c in range(COLS):
      if mat[r][c] == 0:
        q.append([r,c])
      else:
        mat[r][c] = float('inf')

  directions = [[0,1],[0,-1],[1,0],[-1,0]]
  while q:
    x, y = q.popleft()

    for r, c in directions:
      xx, yy = x+r, y+c
      if -1 < xx < ROWS and -1 < yy < COLS and mat[xx][yy] > mat[x][y] + 1:
        mat[xx][yy] = mat[x][y] + 1
        q.append([xx, yy])
  return mat

# print(updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
print(updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))