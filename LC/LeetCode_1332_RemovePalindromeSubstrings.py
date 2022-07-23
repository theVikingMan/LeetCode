def removePalindromeSub(s):
  l, r = 0, len(s) - 1
  while l <= r:
    if s[l] != s[r]:
      return 2
    l += 1
    r -= 1
  return 1

# The only way you can return 1 is if the original string is a palindrome
# Else, you will have to make a total of 2 modifications
# Look at the examples / tc with result of 1 and result of 2