def busyStudent(startTime, endTime, queryTime):
    counter = 0
    for i in range(len(startTime)):
        student = range(startTime[i], endTime[i]+1)
        if queryTime in student:
            counter += 1
    return counter

    


print(busyStudent([9,8,7,6,5,4,3,2,1], [10,10,10,10,10,10,10,10,10], 5))