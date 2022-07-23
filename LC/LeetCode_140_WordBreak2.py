
def wordBreak(s, wordDict):
  dp = {}

  def helper(i):
    if i == len(s):
      return [[]]
    if i in dp:
      return dp[i]

    outcome = []
    for w in wordDict:
      wLen = len(w)
      if i + wLen <= len(s) and s[i:i+wLen] == w:
        combos = helper(i+wLen)
        for postfix in combos:
          outcome.append([w] + postfix)
    dp[i] = outcome
    return dp[i]

  outcome = helper(0)
  res = []
  for strs in outcome:
    res.append(" ".join(strs))
  return res

print(wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))

# def wordBreak(s, wordDict):
#   res = []

#   def helper(i, curr):
#     if i == len(s):
#       res.append(" ".join(curr))
#       return

#     for w in wordDict:
#       wLen = len(w)
#       if i + wLen <= len(s) and s[i:i+wLen] == w:
#         helper(i+wLen, curr + [w])

#   helper(0, [])
#   return res