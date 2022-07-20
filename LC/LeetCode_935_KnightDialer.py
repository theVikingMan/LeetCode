
def knightDialer(n):
	# paths represents every key we can go to from given key
	# -1 is starting condition, we can start from any key
  paths = {-1: [0,1,2,3,4,5,6,7,8,9], 0: [4,6], 1: [6,8], 2: [7,9],
  3: [4,8], 4: [0,3,9], 5: [], 6: [0,1,7], 7: [2,6], 8: [1,3], 9: [2,4] }
  dp = {}

  def helper(idx, curr):
    if idx == 0:
      return 1
    if (idx, curr) in dp:
      return dp[(idx, curr)]
    combos = 0
    for num in paths[curr]:
      combos += helper(idx-1, num)
    dp[(idx, curr)] = combos
    return dp[(idx, curr)]

  mod = (10 ** 9 + 7)
  return helper(n, -1) % mod


# -------------- Classic recursion (TLE) -------------- #

# def knightDialer(n):
#   board = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
#   ROWS, COLS = len(board), len(board[0])
#   dp = {}

#   def helper(r, c, length):
#     if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] == -1:
#       return 0
#     if length == n:
#       return 1
#     if (r, c, length) in dp:
#       return dp[(r, c, length)]

#     directions = [[2, 1], [1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1], [-1, 2]]

#     combos = 0
#     for x, y in directions:
#       rx, cy = r + x, c + y
#       if 0 <= rx < ROWS and 0 <= cy < COLS and board[rx][cy] != -1:
#         combos += helper(rx, cy, length + 1)
#     dp[(r, c, length)] = combos
#     return dp[(r, c, length)]

#   res = 0
#   for r in range(ROWS):
#     for c in range(COLS):
#       res += helper(r, c, 1)
#   mod = 10**9 + 7
#   return res % mod