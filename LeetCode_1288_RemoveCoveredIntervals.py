def removeCoveredIntervals(intervals):
    intervals.sort(key=lambda i : i[0])
    result = [intervals[0]]

    for (start, end) in intervals[1:]:
        # Checking if the next interval is completely covered by most recent result interval
        # If so, just skip
        if ((start >= result[-1][0]) and (end <= result[-1][1])):
            continue
        # Checking if the next interval completely covers the most recent result interval
        # If so, replace most recent interval
        if ((start <= result[-1][0]) and (end >= result[-1][1])):
            result[-1] = [start, end]
        # not covered completely, append
        else:
            result.append([start, end])


    return len(result)

print(removeCoveredIntervals([[1,4],[3,6],[2,8]]))