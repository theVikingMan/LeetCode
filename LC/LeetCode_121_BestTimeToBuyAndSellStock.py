def maxProfit(prices):
    maxMade = 0
    low = float('inf')
    for p in prices:
        tempProfit = p - low
        maxMade = max(tempProfit, maxMade)
        if p < low:
            low = p
    return maxMade

print(maxProfit([7,6,4,3,1]))