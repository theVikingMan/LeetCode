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
          num in squares[(r // 3, c // 3)]):
          return False
      rows[r].add(num)
      cols[c].add(num)
      squares[(r // 3, c // 3)].add(num)
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