def maxProfit(prices):
    maxMade= 0
    low = prices[0]
    for p in prices[1:]:
        tempProfit = p - low
        maxMade = max(tempProfit, maxMade)
        if p < low:
            low = p
    return maxMade

print(maxProfit([7,6,4,3,1]))