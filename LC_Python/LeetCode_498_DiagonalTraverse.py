def solution(mat):
  ROWS, COLS = len(mat), len(mat[0])
  output = []
  res = [[] for _ in range(ROWS + COLS - 1)]
  for r in range(ROWS):
    for c in range(COLS):
      res[r + c].append(mat[r][c])

  for i, g in enumerate(res):
    if i % 2 == 0:
      res[i] = res[i][::-1]
    for n in res[i]:
      output.append(n)

  return output

print(solution([[1,2,3],[4,5,6],[7,8,9]]))