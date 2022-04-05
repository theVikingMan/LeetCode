def numDecodings(s):
    # I - only positive integers
    #       each combination can only be up to the value of 26
    #       26 is valid as z
    # O - Intger: number of ways to decode
    #       Permutations, but no duplicate combinations
    # E - leading zeros are not allowed but dont break
    #       Make the surronding nums not allowed

    # Base case and what will hold our caching. HMs are O(1) look up
    # Initialize as the whole string is considered at least 1 way to decode
    dp = { len(s) : 1 }

    # bottoms up approach to DP
    for i in range(len(s) -1, -1,- 1):
        # check if we CAN'T make any combos up to this point
        if s[i] == '0':
            dp[i] = 0
        # if we can, say we can current divid each char
        else:
            dp[i] = dp[i+1]

        # This is where the numerous ways come into play
        # We currently have 1 as ways to combine but can. We increase based on a 2 digit decode
        # Is it within bounds, 1s are always good but 2s can only be up to 26

        if (i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456'))):
            dp[i] += dp[i+2]

    # Given bottoms-up approach, this value should hold the result
    return dp[0]

print(numDecodings('226'))