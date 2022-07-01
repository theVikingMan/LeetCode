def subarraySort(array):
    res = [-1, -1]
    minNum = float('inf')
    maxNum = float('-inf')
    for i, num in enumerate(array):
        if outOfOrder(i, num, array):
            minNum = min(minNum, num)
            maxNum = max(maxNum, num)
    if minNum == float('inf'):
        return res
    l = 0
    while array[l] <= minNum:
        l += 1
    res[0] = l

    r = len(array) - 1
    while array[r] >= maxNum:
        r -= 1
    res[1] = r
    return res

def outOfOrder(i, num, array):
    if i == 0:
        return num > array[i+1]
    if i == len(array) - 1:
        return num < array[i-1]
    if 0 <= i < len(array) - 1:
        return (array[i-1] > num) or (array[i+1] < num)

# T: O(n) -> n is number of elements.
# S: O(1) -> Using only pointers

print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))