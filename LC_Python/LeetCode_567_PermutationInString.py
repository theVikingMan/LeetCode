def checkInclusion(p, s):
  countP = [0 for _ in range(26)]
  for l in p:
    countP[ord(l) - ord("a")] += 1

  countS = [0 for _ in range(26)]

  l, n = 0, len(p)
  for r in range(len(s)):
    countS[ord(s[r]) - ord("a")] += 1
    while r - l + 1 >= n:
      if countS == countP:
        return True
      countS[ord(s[l]) - ord("a")] -= 1
      l += 1
  return False if countS != countP else True

print(checkInclusion("ab","eidbaooo"))


# -------------- Sub optimal (26 * n) -------------- #
import collections

def solution(s1, s2):
  if len(s1) > len(s2):
    return False

  count1, count2 = collections.Counter(s1), {}

  l = 0
  for r in range(len(s2)):
    if count1 == count2:
      return True
    count2[s2[r]] = 1 + count2.get(s2[r], 0)
    while l < r and (r - l + 1) > len(s1):
      count2[s2[l]] -= 1
      if count2[s2[l]] == 0:
        del count2[s2[l]]
      l += 1

  return False if count1 != count2 else True