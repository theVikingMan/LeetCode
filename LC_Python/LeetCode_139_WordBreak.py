def wordBreak(s, wordDict):
    # Initialize each state to False as that is there base state
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True # set base value if the end can be reached

    for i in range(len(s) - 1, -1, -1): # Work backwards on the given string
        for w in wordDict:
            n = len(w)
            if (i + n <= len(s) and s[i: i+n] == w): # Inbounds and same word
                # Want to track that it is possible not just with current word and place
                # But as well with the +1 state
                dp[i] = dp[i + len(w)]
            if dp[i]: # making sure not to override a True state (old mistake)
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