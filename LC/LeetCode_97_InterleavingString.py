def isInterleave(s1, s2, s3):
  if len(s1) + len(s2) != len(s3):
    return False
  dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
  dp[len(s1)][len(s2)] = True

  for i in range(len(s1), -1, -1):
    for j in range(len(s2), -1, -1):
      if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
        dp[i][j] = True
      if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
        dp[i][j] = True
  return dp[0][0]

print(isInterleave("aac", "dba", "aadbca"))

# -------------------- Recursive with Cache -------------------- #

# def isInterleave(s1, s2, s3):
    # if len(s1) + len(s2) != len(s3):
    #   return False
    # cache = {}

    # def helper(i, j):
    #   s3Idx = i + j
    #   if i == len(s1) and j == len(s2):
    #     return True
    #   if (i, j) in cache:
    #     return cache[(i, j)]

    #   outcome = False
    #   if i < len(s1) and s1[i]  == s3[s3Idx]:
    #     outcome = helper(i+1, j)
    #   if j < len(s2) and s2[j] == s3[s3Idx]:
    #     outcome = outcome or helper(i, j+1)

    #   cache[(i, j)] = outcome
    #   return outcome

    # return helper(0, 0)

# print(isInterleave("aac", "dba", "aadbca"))
