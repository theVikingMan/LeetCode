def minMeetingRooms(intervals):
    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])
    # res will be the maxing function and count will be the
    # current counter keeper
    res, count = 0, 0
    s, e = 0, 0

    while s < len(intervals):
        if start[s] < end[e]: # a meeting has started before another has ended
            s += 1
            count += 1
        else: # one of the started meetings just ended
            e += 1
            count -= 1
        res = max(count, res)
    return res

print(minMeetingRooms([[0,30],[5,10],[15,20]]))