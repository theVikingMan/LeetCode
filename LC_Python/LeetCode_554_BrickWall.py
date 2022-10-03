def leastBricks(wall):
  gapCount = {0 : 0} # incase of only 1 column (see exmp)

  for r in wall:
    total = 0 # the gaps are between bricks (on the right)
    for brick in r[:-1]:
      total += brick # Calcs the gap pos
      gapCount[total] = 1 + gapCount.get(total, 0)
    print(gapCount)

  return len(wall) - max(gapCount.values()) # total rows minus the max num of gaps
