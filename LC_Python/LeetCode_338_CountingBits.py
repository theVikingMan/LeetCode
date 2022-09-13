def countBits(n):
  offset = 1
  res = [0]

  for num in range(1, n + 1):
    if num == offset * 2:
      offset *= 2
    res.append(1 + res[num - offset])
  return res

print(countBits(10))
