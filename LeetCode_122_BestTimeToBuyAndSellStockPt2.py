def maxProfit(prices):
    max_profit = 0
    for i in range(len(prices) - 1):
        max_profit += max(prices[i+1] - prices[i], 0)
    return max_profit

print(maxProfit([1,5,7,3,3,8]))