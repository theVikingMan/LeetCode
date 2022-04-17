def solution(s):
  # create set to hold all the seen values in our window
  seenSet = set()
  res = 0
  l = 0
  # creates our right pointer
  for r in range(len(s)):
    while s[r] in seenSet:
      seenSet.remove(s[l])
      l += 1
    seenSet.add(s[r])
    res = max(res, r - l + 1)
  return res

print(solution('bbbb'))