def merge(intervals):
    intervals.sort(key=lambda i:i[0])
    result = [intervals[0]]

    for start, end in intervals[1:]:
        prev = result[-1] # Compare to the most recent result array
        # overlap -> the next intervals start in lower than prev
        if start <= prev[1]:
            prev[1] = max(prev[1], end)
        else:
            result.append([start, end]) # non overlap, add new interval
    return result

