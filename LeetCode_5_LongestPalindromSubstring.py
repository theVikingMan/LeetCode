def longestPalindrome(s):
  res = ''
  resLen = 0

  # loop over all the letter to see al the possible combinations
  for i in range(len(s)):
    # odd length
    l, r = i, i
    # while in bounds and a palendrom
    while l >=0 and r < len(s) and (s[l] == s[r]):
      if (r - l + 1) > resLen:
        resLen = (r - l + 1)
        res = s[l:r+1]
      r += 1
      l -= 1

    # even length
    l, r = i, i + 1
    while l >=0 and r < len(s) and (s[l] == s[r]):
      if (r - l + 1) > resLen:
        resLen = (r - l + 1)
        res = s[l:r+1]
      r += 1
      l -= 1

  return res

print(longestPalindrome("cbc"))
print(longestPalindrome("bbaaa"))
print(longestPalindrome("abnba"))