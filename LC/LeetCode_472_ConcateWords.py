

def findAllConcatenatedWordsInADict(words):
  seen = set(words)
  dp = {}

  def dfs(s):
    if s in dp:
      return dp[s]
    dp[s] = False
    for i in range(1, len(s)):
      prefix = s[:i]
      postfix = s[i:]

      if prefix in seen and postfix in seen:
        dp[s] = True
        return True
      if prefix in seen and dfs(postfix):
        dp[s] = True
        return True
    return dp[s]
  return [word for word in words if dfs(word)]

# ------------ Using word break (TLE) ----------- #

def findAllConcatenatedWordsInADict(words):
  words.sort(key=lambda i:len(i))
  cache = set()
  res = []

  def isValidCon(s):
    dp = [False for _ in range(len(s) + 1)]
    dp[-1] = True

    for i in range(len(s) -1, -1, -1):
      for w in cache:
        wLen = len(w)
        if i + wLen <= len(s) and s[i:i+wLen] == w:
          dp[i] = dp[i+wLen]
        if dp[i]:
          break
    return dp[0]

  for word in words:
    if isValidCon(word):
      res.append(word)
    cache.add(word)
  return res
