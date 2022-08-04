
def findAnagrams(s, p):
  sCount, pCount = [0] * 26, [0] * 26
  res = []
  for letter in p:
    pCount[ord(letter) - ord('a')] += 1
  pLen = len(p)

  l = 0
  for r, letter in enumerate(s):
    sCount[ord(letter) - ord('a')] += 1
    while l <= r and r - l + 1 >= pLen:
      if sCount == pCount:
        res.append(l)
      sCount[ord(s[l]) - ord('a')] -= 1
      l += 1
  return res

print(findAnagrams("cbaebabacd", "abc"))
print(findAnagrams("cbaebabacd", "c"))