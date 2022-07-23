

def candyCrush(board):
  # error checking
  if not board:
    return board

  ROWS, COLS = len(board), len(board[0])

  done = True
  # STEP 1: crush rows using Sliding Window
  for r in range(ROWS):
    for c in range(COLS - 2):
      elem1 = abs(board[r][c])
      elem2 = abs(board[r][c + 1])
      elem3 = abs(board[r][c + 2])
      if elem1 == elem2 and elem2 == elem3 and elem1 != 0:
        board[r][c] = -1 * elem1
        board[r][c + 1] = -1 * elem2
        board[r][c + 2] = -1 * elem3
        done = False

  # STEP 2: crush columns
  for c in range(COLS):
    for r in range(ROWS - 2):
      elem1 = abs(board[r][c])
      elem2 = abs(board[r + 1][c])
      elem3 = abs(board[r + 2][c])
      if elem1 == elem2 and elem2 == elem3 and elem1 != 0:
        board[r][c] = -1 * elem1
        board[r + 1][c] = -1 * elem2
        board[r + 2][c] = -1 * elem3
        done = False

  # STEP 3: gravity
  if not done:
    for c in range(COLS):
      idx = ROWS - 1
      for r in range(ROWS -1, -1, -1):
        # move all positive numbers down
        if board[r][c] > 0:
          board[idx][c] = board[r][c]
          idx -= 1
        # drop 0's from the top
      for r in range(idx, -1, -1):
        board[r][c] = 0

  return board if done else candyCrush(board)


print(candyCrush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]))