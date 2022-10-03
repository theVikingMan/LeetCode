import collections

def isValidSudoku(board):
  seenValues = collections.defaultdict(set)

  ROWS, COLS = len(board), len(board[0])
  for r in range(ROWS):
    for c in range(COLS):
      element = board[r][c]
      if element == ".": continue
      if element in seenValues[r] or element in seenValues[c] or element in seenValues[(r // 3, c // 3)]:
        return False
      seenValues[r].add(element)
      seenValues[c].add(element)
      seenValues[(r // 3, c // 3)].add(element)

  return True

print(isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))