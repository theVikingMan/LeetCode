import collections

def countPalindromicSubsequence(s):
  res = set()
  left = set()
  right = collections.Counter(s)

  for middle in range(len(s)):
    right[s[middle]] -= 1
    if right[s[middle]] == 0:
      right.pop(s[middle])

    for i in range(26):
      letter = chr(ord("a") + i)
      if letter in left and letter in right:
        res.add((s[middle], letter))

    left.add(s[middle])

  return len(res)