import collections

def minWindow(s, t):
  if len(s) < len(t) or t == "":
    return ""
  l = 0
  tCount = collections.Counter(t)
  resCount = {}
  have, need = 0, len(tCount)
  res, resLen = [-1, -1], float('inf')

  for r in range(len(s)):
    c = s[r] # get the current character
    resCount[c] = 1 + resCount.get(c, 0) # mark that we have seen another instance of the char
    if resCount[c] == tCount[c]: # do we have the exact amount of chars for the res string
      have += 1

    while have == need:
      if (r - l + 1) < resLen:
        res = [l, r]
        resLen = r - l + 1
      if s[l] in resCount:
        resCount[s[l]] -= 1
        if resCount[s[l]] < tCount[s[l]]: # did we just lose a needed char from the left side coming in
          have -= 1 # mark that we lost a needed letter
      l += 1 # narrow window from left side
  l, r = res
  return s[l:r+1] if resLen != float('inf') else ""

# print(minWindow("ADOBECODEBANC", "ABC"))
# print(minWindow("a", "a"))
print(minWindow('aa', 'aa'))