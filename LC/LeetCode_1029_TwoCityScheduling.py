def twoCitySchedCost(costs):
  diffs = []
  for c1,c2 in costs:
    diffs.append([c2 - c1, c1, c2])
    # Negative diffs mean more adv to go city B, positive mean go city A

  diffs.sort()
  res = 0
  print(diffs)
  for i in range(len(diffs)):
    if i < len(diffs) // 2:
      res += diffs[i][2]
    else:
      res += diffs[i][1]
  return res
