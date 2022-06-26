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
        helper(i+1, j+1),
        helper(i, j+1),
        helper(i+1, j))

    return dp[(i, j)]

  return helper(0, 0)

print(minDistance("intention", "execution"))

# T: O(m * n) -> m being the length of first word, n being the length of second word
# O: O(m * n)