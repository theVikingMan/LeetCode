def eraseOverlapIntervals(intervals):
    intervals.sort(key = lambda i : i[0])
    res = 0
    prevEnd = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            res += 1
            prevEnd = min(end, prevEnd)
    return res

print(eraseOverlapIntervals(
  [[1,100],[11,22],[1,11],[2,12]]
))