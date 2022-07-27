def solution(strs):
  res = ""

  for i in range(len(strs[0])):
    for w in strs:
      # Not valid if word is not long enough or letter doesn't match
      if len(w) == i or w[i] != strs[0][i]:
        return res
    res += strs[0][i]
  return res

print(solution(["flower","flow","flight"]))