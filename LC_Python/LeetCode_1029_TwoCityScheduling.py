def twoCitySchedCost(costs):
  diffs = []
  for c1,c2 in costs:
    diffs.append([c2 - c1, c1, c2])
    # Negative diffs mean more adv to go city B, positive mean go city A

  diffs.sort() # will sort on first subarray num
  res = 0

  for i in range(len(diffs)):
    if i < len(diffs) // 2: # negative or small num == perfer city B
      res += diffs[i][2]
    else:                   # Once we have 1/2 the people, start taking the other half
      res += diffs[i][1]
  return res
