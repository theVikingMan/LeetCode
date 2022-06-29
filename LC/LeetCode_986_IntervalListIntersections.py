def intervalIntersection(firstList, secondList):
    if not firstList or not secondList:
        return []
    res = []
    i, j = 0, 0

    # While we still have elements in both elements to evaluate
    while i < len(firstList) and j < len(secondList):
        # check the max of left => the beginning of the start of a result
        # check also the min of the right => end of the result
        l = max(firstList[i][0], secondList[j][0]) # max of starts
        r = min(firstList[i][1], secondList[j][1]) # min of ends

        if l <= r: # Proper overlapping of intervals
            res.append([l, r])

        # move pointers based on ending values
        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1

    return res

print(intervalIntersection([[0,2],[5,10],[13,23],[24,25]],
                           [[1,5],[8,12],[15,24],[25,26]]))