import collections


def isToeplitzMatrix(matrix):
  ROWS, COLS = len(matrix), len(matrix[0])

  for r in range(ROWS):
    for c in range(COLS):
      if not (r - 1 == -1 or c - 1 == -1) or not matrix[r-1][c-1] == matrix[r][c]:
        continue
      else:
        return False
  return True

# ------------------ Alternative Method ------- #

def isToeplitzMatrix(matrix):
  tracker = collections.defaultdict(list)
  ROWS, COLS = len(matrix), len(matrix[0])

  for r in range(ROWS):
    for c in range(COLS):
      if len(tracker[(r-c)]) < 1 or tracker[(r-c)][-1] == matrix[r][c]:
        tracker[(r-c)].append(matrix[r][c])
      else:
        return False
  return True

print(isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))