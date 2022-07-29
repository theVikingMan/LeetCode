def longestPalindromeSubseq(s):
  dp = {}

  def helper(l, r):
    if l == r:
      return 1
    if l > r:
      return 0
    if (l, r) in dp:
      return dp[(l, r)]

    outcome = 0
    if s[l] == s[r]:
      same = 2 + helper(l+1, r-1)
      outcome = max(outcome, same)
    else:
      left = helper(l+1, r)
      right = helper(l, r-1)
      outcome = max(outcome, left, right)
    dp[(l, r)] = outcome
    return dp[(l, r)]

  return helper(0, len(s) - 1)

print(longestPalindromeSubseq('abbaa'))