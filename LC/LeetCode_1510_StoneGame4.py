def winnerSquareGame(n):
  dp = {}

  def dfs(i):
    if i == 0:
      return False
    if i == 1:
      return True
    if i in dp:
      return dp[i]

    upperBound = int(i ** 0.5)
    dp[i] = False
    for j in range(1, upperBound + 1):
      if not dfs(i - (j * j)):
        dp[i] = True
        break
    return dp[i]
  return dfs(n)