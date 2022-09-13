def minDays(n):
  dp = {0 : 0, 1 : 1}

  def dfs(num):
    if num in dp:
      return dp[num]

    one = 1 + (num % 2) + dfs(num // 2)
    two = 1 + (num % 3) + dfs(num // 3)

    dp[num] = min(one, two)
    return dp[num]

  return dfs(n)

print(minDays(10))


# --------- DFS with Memoization (TLE) ------- #

# def minDays(n):
#   dp = {0 : 0, 1 : 1}

#   def dfs(num):
#     if num in dp:
#       return dp[num]

#     outcome = 1 + dfs(num - 1)
#     if num % 2 == 0:
#       two = 1 + dfs(num // 2)
#       outcome = min(outcome, two)
#     if num % 3 == 0:
#       three = 1 + dfs(num // 3)
#       outcome = min(outcome, three)
#     dp[num] = outcome
#     return dp[num]
#   return dfs(n)