import collections

def solution(board):
  rows = collections.defaultdict(set)
  cols = collections.defaultdict(set)
  squares = collections.defaultdict(set)

  for r in range(9):
    for c in range(9):
      num = board[r][c]
      if num == '.':
        continue
      if (num in rows[r] or
          num in cols[c] or
          num in squares[(r // 3, c // 3)]): # Invalid: num is already in row or column or in the same sub-square
          return False
      rows[r].add(num) # mark it as seen and valid
      cols[c].add(num) # mark it as seen and valid
      squares[(r // 3, c // 3)].add(num) # mark it as seen and valid
  return True

print(solution([["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]]))