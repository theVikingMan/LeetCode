import collections

def findAnagrams(s, p):
  sCount = [0] * 26
  pCount = [0] * 26
  res = []
  for l in p:
    pCount[ord(l) - ord('a')] += 1
  pLen = len(p)

  for i in range(len(s)):
    sCount[ord(s[i]) - ord('a')] += 1
    if i + 1 >= pLen:
      if sCount == pCount:
        res.append(i - pLen + 1)
      sCount[ord(s[i - pLen + 1]) - ord('a')] -= 1

  return res

print(findAnagrams("cbaebabacd", "abc"))