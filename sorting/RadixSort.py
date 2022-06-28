def radixSort(array):
    if len(array) == 0:
        return array
    maxNumber = max(array)
    digit = 0
    while maxNumber / (10 ** digit) > 0:
        countingSort(array, digit)
        digit += 1
    return array

def countingSort(array, digit):
    sortedArray = [0] * len(array) # output array with digit sorted nums
    countArray = [0] * 10 # base 10 num system. Counts nums by digit

    digitColumn = 10 ** digit # gets you the 10's place number to divid by
    for num in array: # mark each digit place from each number
        countIdx = (num // digitColumn) % 10 # grabs 10's place number
        countArray[countIdx] += 1

    for i in range(1, 10):
        countArray[i] += countArray[i - 1]

    # going backwards maintains stable sorting property
    for i in range(len(array) - 1, -1, -1):
        countIdx = (array[i] // digitColumn) % 10
        countArray[countIdx] -= 1
        sortedIdx = countArray[countIdx]
        sortedArray[sortedIdx] = array[i]

    for i in range(len(array)):
        array[i] = sortedArray[i]

print(radixSort([8762, 654, 3008, 345, 87, 65, 234, 12, 2]))

# T: O(d * (n + b))
# S: O(n + b)
