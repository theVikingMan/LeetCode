
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
  def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
    res = []
    sortedTemp = []
    # flatten all the intervals into one array
    for i in schedule:
      for j in i:
        sortedTemp.append([j.start, j.end])
    # sort by first integer
    sortedTemp.sort(key=lambda i:i[0])
    mergedTemp = [sortedTemp[0]]
    # merge all over lapping intervals
    for s, e in sortedTemp[1:]:
      prev = mergedTemp[-1]
      if s <= prev[1]:
        prev[1] = max(e, prev[1])
      else:
        mergedTemp.append([s, e])
    # all thats left are the gaps in the intervals
    for i in range(len(mergedTemp) - 1):
      curr, nxt = mergedTemp[i], mergedTemp[i+1]
      newInt = Interval(curr[1], nxt[0])
      res.append(newInt)
    return res