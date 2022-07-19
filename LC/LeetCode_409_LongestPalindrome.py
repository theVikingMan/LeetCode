def longestPalindrome(s):
  odds = set()

  for letter in s:
    if letter in odds:
      odds.remove(letter)
    else:
      odds.add(letter)

  if len(odds) > 0:
    return len(s) - len(odds) + 1
  else:
    return len(s)