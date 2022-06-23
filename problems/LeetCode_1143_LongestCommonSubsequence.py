def longestCommonSubsequence(text1, text2):
  dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

  for i in range(len(text1) - 1, -1, -1):
    for j in range(len(text2) - 1, -1, -1):
      if text1[i] == text2[j]:
        dp[i][j] = 1 + dp[i + 1][j + 1]
      else:
        dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
  return dp[0][0]

print(longestCommonSubsequence("abcde", "ace"))

# --------------- Recursion with Memoization -------------- #

def longestCommonSubsequence(text1, text2):
  cache = {}

  def dp(i, j):
    if i == len(text1) or j == len(text2):
      return 0
    if (i, j) in cache:
      return cache[(i, j)]

    if text1[i] == text2[j]:
      cache[(i, j)] = 1 + dp(i + 1, j + 1)
    else:
      cache[(i, j)] = max(dp(i, j + 1), dp(i + 1, j))

    return cache[(i, j)]

  return dp(0, 0)

print(longestCommonSubsequence("abcde", "ace"))

