def hasAllCodes(s, k):
  count = set()
  for i in range(len(s) - k + 1):
    count.add(s[i: i+k])

  return 2 ** k == len(count)