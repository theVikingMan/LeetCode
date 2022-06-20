def wordBreak(s, wordDict):
    # Initialize each state to False as that is there base state
    dp = [False] * (len(s) + 1)
    #
    dp[len(s)] = True
    # Work backwards on the given string
    for i in range(len(s) - 1, -1, -1):
        # At each letter in the given string, check each word
        for w in wordDict:
            # Inialize the word length for word check at current state
            n = len(w)
            # Inbounds and same word...
            if (i+n <= len(s) and s[i:i+n] == w):
                # Want to track that it is possible not just with current word and place
                # But as well with the +1 state
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break

    return dp[0]

print(wordBreak("leetcode", ["leet","code"]))

# -------------- Recursion with memoization ----------- #

# def wordBreak(s, wordDict):
#     wDict = set(wordDict)
#     memo = {}
#     def dfs(sMod):
#       if sMod == "":
#         return True
#       if sMod in memo:
#         return memo[sMod]

#       for w in wordDict:
#         wLen = len(w)
#         if wLen <= len(sMod) and sMod[:wLen] in wDict:
#           if dfs(sMod[wLen:]):
#             memo[sMod] = True
#             return memo[sMod]
#       memo[sMod] = False
#       return memo[sMod]

#     dfs(s)
#     return memo[s]