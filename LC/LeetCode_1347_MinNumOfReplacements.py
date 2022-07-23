import collections

def minSteps(s, t):
  sCount = collections.Counter(s)
  res = 0

  for l in t:
    if sCount[l] > 0:
      sCount[l] -= 1
    else:
      res += 1
  return res


print(minSteps('aabba', 'abccd'))