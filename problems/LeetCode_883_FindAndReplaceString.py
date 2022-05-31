def findReplaceString(s, indices, sources, targets):
  lookup = { i:[src, tar] for i, src, tar in zip(indices, sources, targets) }
  i, res = 0, ''
  while i < len(s):
    if i in lookup and s[i:].startswith(lookup[i][0]):
      res += lookup[i][1]
      i += len(lookup[i][0])
    else:
      res += s[i]
      i += 1
  return res

print(findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]))