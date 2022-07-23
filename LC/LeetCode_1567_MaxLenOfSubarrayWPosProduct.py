from collections import Counter
import itertools

def getMaxLen(nums):
  resLen, pos, neg = 0, 0, 0

  for n in nums:
    if n > 0:
      pos = 1 + pos
      neg = 1 + neg if neg else 0
    elif n < 0:
      pos, neg = 1 + neg if neg else 0, 1 + pos
    else:
      pos = neg = 0

    resLen = max(resLen, pos)

  return resLen

print(getMaxLen([1,-2,-3,4]))