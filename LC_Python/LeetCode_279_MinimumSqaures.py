import math

def numSquares(n):
  dp = [float('inf') for _ in range(n+1)]
  square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
  dp[0] = 0

  for i in range(1, n+1):
    for num in square_nums:
      if i < num:
        break
      dp[i] = min(dp[i-num] + 1, dp[i])

  return dp[-1]

print(numSquares(12))

# ----------------- Recursion w/ Memoization (TLE) ------------- #

# def numSquares(n):
#   squares = [i**2 for i in range(1, int(math.sqrt(n) + 1))]
#   cache = {}

#   def helper(k):
#     if k in squares:
#       return 1
#     if k in cache:
#       return cache[k]

#     minRes = float('inf')
#     for sq in squares:
#       if k < sq:
#         break
#       newNum = helper(k - sq) + 1
#       minRes = min(minRes, newNum)
#     cache[k] = minRes
#     return cache[k]
#   return helper(n)