def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda i:i[0])
    res = [intervals[0]]
    for start, end in intervals[1:]:
        prev = res[-1]
        if start <= prev[1]:
            res[-1][1] = max(prev[1], end)
        else:
            res.append([start, end])
    return res

print(mergeOverlappingIntervals([
  [1, 2],
  [3, 5],
  [4, 7],
  [6, 8],
  [9, 10]
]))