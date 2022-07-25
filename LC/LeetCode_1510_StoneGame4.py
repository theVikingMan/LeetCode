def winnerSquareGame(n):
  dp = {}

  def dfs(i): # i is the game state on THAT players turn
    if i == 0: # if its my turn and i is zero, then other player wone
      return False
    if i == 1: # if its my turn and i is one, then other player will lose on next turn
      return True
    if i in dp:
      return dp[i]

    upperBound = int(i ** 0.5)
    dp[i] = False
    for j in range(1, upperBound + 1):
      if not dfs(i - (j * j)): # if any possibility of the other player lossing, I win
        dp[i] = True
        break
    return dp[i]
  return dfs(n)