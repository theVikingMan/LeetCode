def findMinArrowShots(points):
    # Overall: Check if a new arrow is needed
    # by if the same arrow wont hit the start of the next
    arrows = 1
    points.sort(key=lambda x:x[1])
    first_end = points[0][1]

    for start, end in points[1:]:
        if start > first_end:
            arrows += 1
            first_end = end
    return arrows

print(findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))

