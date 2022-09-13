def findMinDifference(timePoints):
    minArr = []
    res = float('inf')
    for i, time in enumerate(timePoints):
      hours, mins = time.split(':')
      totalMins = (60 * int(hours)) + (int(mins))
      minArr.append(totalMins)
    minArr.sort()
    for i in range(len(minArr) - 1):
      res = min(res, (minArr[i+1] - minArr[i]))

    res = min(res, (abs(1440 + minArr[0]) - minArr[-1]))
    return res