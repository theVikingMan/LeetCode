def maximumEvenSplit(finalSum):
  if finalSum % 2:
    return []
  res = []
  s = 0

  for i in range(1, finalSum // 2 + 1):
    even = i * 2
    s += even
    res.append(even)
    if s == finalSum:
      return res
    if s > finalSum:
      diff = s - finalSum
      res.pop(res.index(diff))
      return res

print(maximumEvenSplit(78))