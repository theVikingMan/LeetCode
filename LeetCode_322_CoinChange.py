def coinChange(coins, amount):
    # Initialize every state from 0 to N to track min coins for each state
    dp = [amount + 1] * (amount + 1)
    # Base state is 0 which we need 0 coins to make up
    dp[0] = 0

    # start seeing if we can make 1 with our coins up to N
    for a in range(1, amount + 1):
        # checking each coin...
        for c in coins:
            # Will our current coin have a remainder that we need to check
            # the min amount of coins for that remainder
            if a - c >= 0:
                # take the min of the current coin count (default is N)
                # but it also will look through all the combinations of the coins
                # that we have
                dp[a] = min(dp[a], 1 + dp[a-c])

    return dp[amount] if dp[amount] != amount + 1 else -1


print(coinChange([1,2,3], 10))