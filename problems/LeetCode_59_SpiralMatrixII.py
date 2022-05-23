def solution(n):
  if n < 1: # Invalid possible matrix
    return []
  res = [[0 for _ in range(n)] for _ in range(n)] # create result array with dummy values
  l = t = 0
  r = b = n
  num = 1

  while l < r and t < b: # while our pointers haven't over lapped
    for i in range(l, r): # left to right
      res[t][i] = num
      num += 1
    t += 1

    for i in range(t, b): # top to bottom
      res[i][r - 1] = num
      num += 1
    r -= 1

    if not (l < r and t < b): # check edge cases if we have a single row / column
      break

    for i in range(r - 1, l - 1, -1): # left to right
      res[b - 1][i] = num
      num += 1
    b -= 1

    for i in range(b - 1, t - 1, -1): # bottom to top
      res[i][l] = num
      num += 1
    l += 1
  return res

print(solution(3))
print(solution(1))
print(solution(0))