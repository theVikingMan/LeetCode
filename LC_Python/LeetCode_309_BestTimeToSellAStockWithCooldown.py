def maxProfit(prices):
  if len(prices) < 2:
    return 0
  dp = {}


  def dfs(i, canBuy):
    if i >= len(prices):
      return 0
    if (i, canBuy) in dp:
      return dp[(i, canBuy)]

    cooldown = dfs(i + 1, canBuy)
    if canBuy:
      buy = dfs(i + 1, not canBuy) - prices[i]
      dp[(i, canBuy)] = max(cooldown, buy)
    else:
      sell = dfs(i + 2, not canBuy) + prices[i]
      dp[(i, canBuy)] = max(cooldown, sell)

    return dp[(i, canBuy)]

  return dfs(0, True)

print(maxProfit([1,2,3,0,2]))
print(maxProfit([3, 4, 2, 6, 2, 4, 6]))