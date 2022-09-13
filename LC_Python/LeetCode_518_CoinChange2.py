# --------- OPTIMIZED DP --------- #

def change(amount, coins):
  dp = [0] * (amount + 1)
  dp[0] = 1

  for i in range(len(coins) - 1, -1, -1):
    newDP = [0] * (amount + 1)
    newDP[0] = 1

    for j in range(1, amount + 1):
      newDP[j] = dp[j]
      if j - coins[i] >= 0:
        newDP[j] += newDP[j - coins[i]]
    dp = newDP
  return dp[amount]

print(change(10, [2, 4])) # Output: 4

# Time: O(n * m)
# Space: O(n)

# --------- NON-OPTIMIZED DP --------- #

# def change(amount, coins):
#   dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

#   for c in range(1, len(coins) + 1):
#     dp[c][0] = 1
#     coin = coins[c-1]
#     for i in range(1, amount + 1):
#       dp[c][i] = dp[c-1][i]
#       if i - coin >= 0:
#         dp[c][i] += dp[c][i - coin]

#   return dp[-1][-1]

# Time: O(n * m)
# Space: O(n * m)

# --------- RECURSIVE WITH MEMOIZATION --------- #

# def change(amount, coins):
#   cache = {}

#   def dfs(i, total):
#     if (i, total) in cache:
#       return cache[(i, total)]
#     if total == amount:
#       return 1
#     if total > amount or i >= len(coins):
#       return 0

#     cache[(i, total)] = dfs(i, total + coins[i]) + dfs(i+1, total)
#     return cache[(i, total)]

#   return dfs(0, 0)

# print(change(500, [3,5,7,8,9,10,11]))

# Time: O(n * m)
# Space: O(n * m)