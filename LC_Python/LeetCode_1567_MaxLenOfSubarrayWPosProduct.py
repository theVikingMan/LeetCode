
def getMaxLen(nums):
  resLen, pos, neg = 0, 0, 0

  for n in nums:
    if n > 0: # another pos means add to pos but
      pos = 1 + pos
      neg = 1 + neg if neg else 0
    elif n < 0: # pos will be 1 or whatever the flipped neg is
      pos, neg = 1 + neg if neg else 0, 1 + pos
    else: # If n == zero, set both counters to 0 as anything muli'd by 0 is 0
      pos = neg = 0

    resLen = max(resLen, pos)

  return resLen

print(getMaxLen([1,-2,-3,4]))

# Kadenes Algo
