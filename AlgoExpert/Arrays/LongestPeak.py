def longestPeak(array):
    res = 0
    for i in range(len(array)):
        if i - 1 >= 0 and i + 1 < len(array) and array[i-1] < array[i] > array[i+1]:
            res = max(res, width(i, array))
    return res


def width(i, array):
    output = 1
    l, r = i-1, i+1
    while l >= 1 and array[l] > array[l - 1]:
        l -= 1
    while r < len(array) -1 and array[r] > array[r+1]:
        r += 1
    output = max(output, r - l + 1)
    return output

# T: O(n) -> n is number of elements. find peaks + find width (NOT NESTED)
# S: O(1) -> Using only pointers

print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))