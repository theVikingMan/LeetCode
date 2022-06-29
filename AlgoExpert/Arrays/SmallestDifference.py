def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    res = float('inf')
    output = []

    o, t = 0, 0
    while o < len(arrayOne) and t < len(arrayTwo):
        oneNum, twoNum = arrayOne[o], arrayTwo[t]
        diff = findDiff(oneNum, twoNum)
        if diff < res:
            res = diff
            output = [oneNum, twoNum]
        if oneNum < twoNum:
            o += 1
        else:
            t += 1
    return output

def findDiff(num1, num2):
    return abs(abs(num1) - abs(num2))

print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))