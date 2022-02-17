def longestPalindrome(s):
  n = len(s)

  def longestPal(l, r):
    nonlocal maxLen, startIndex
    while l-1 >= 0 and r+1 < n and s[l-1] == s[r+1]:
      l -= 1
      r += 1
    newLen = r-l+1
    if newLen > maxLen:
      maxLen = newLen
      startIndex = l

  maxLen = startIndex = 0
  for i in range(n):
    longestPal(i, i)
    if i+1 < n and s[i] == s[i+1]:
      longestPal(i, i+1)

  return s[startIndex: startIndex + maxLen]


print(longestPalindrome("cbc"))