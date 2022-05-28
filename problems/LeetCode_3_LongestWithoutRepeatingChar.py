def solution(s):
  seenSet = set() # create set to hold all the seen values in our window
  res = 0
  l = 0

  for r in range(len(s)): # for loop creates our right pointer
    while s[r] in seenSet:
      seenSet.remove(s[l])
      l += 1
    seenSet.add(s[r])
    res = max(res, r - l + 1)
  return res

print(solution('bbbbaba'))