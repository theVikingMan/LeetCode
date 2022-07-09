
# ----------- DP --------- #

def solution(str1, str2):
    dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

    for j in range(len(str2) + 1):
        dp[len(str1)][j] = len(str2) - j
    for i in range(len(str1) + 1):
        dp[i][len(str2)] = len(str1) - i

    for i in range(len(str1) - 1, -1, -1):
        for j in range(len(str2) - 1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
    return dp[0][0]

# ----------- Recursive with Memoization --------- #

def minDistance(word1, word2):
  dp = {}

  def helper(i, j):
    if i == len(word1) or j == len(word2):
      return max(len(word1) - i, len(word2) - j)
    if (i, j) in dp:
      return dp[(i, j)]

    if i < len(word1) and j < len(word2) and word1[i] == word2[j]:
      dp[(i, j)] = helper(i+1, j+1)
    else:
      dp[(i, j)] = 1 + min(
        helper(i+1, j+1), # replace letter
        helper(i, j+1), # insert letter
        helper(i+1, j)) # delete letter

    return dp[(i, j)]

  return helper(0, 0)

print(minDistance("intention", "execution"))

# T: O(m * n) -> m being the length of first word, n being the length of second word
# O: O(m * n)