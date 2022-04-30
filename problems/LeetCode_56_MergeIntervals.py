def merge(intervals):
    intervals.sort(key = lambda i : i[0])
    result = [intervals[0]]

    # a way of looking at both elements in each interative of intervals
    for start, end in intervals[1:]:
        # Compare to the most recent result array
        prev = result[-1]
        # If we found an overlap -> the next intervals start in lower than the end of the
        # most recent result
        if start <= prev[1]:
            # alter result end for the max
            prev[1] = max(prev[1], end)
        else:
            # We havent found a interval that can be merged, just add it
            result.append([start, end])
    return result

