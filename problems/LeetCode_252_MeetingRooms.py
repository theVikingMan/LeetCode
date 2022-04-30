def canAttendMeetings(intervals):
        intervals.sort(key = lambda i : i[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True

print(canAttendMeetings([[6,15],[13,20],[6,17]]))
