def insert(intervals, newInterval):
  res = []

  for i in range(len(intervals)):
    if newInterval[1] < intervals[i][0]: # new Interval is before -> no overlap with the remaining intervals
      res.append(newInterval)
      return res + intervals[i:]
    elif newInterval[0] > intervals[i][1]: # new Interval is after -> but could overlap with others
      res.append(intervals[i])
    else: # overlapping
      newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
  res.append(newInterval)
  return res

print(insert([[1,3],[6,9]], [2,5]))