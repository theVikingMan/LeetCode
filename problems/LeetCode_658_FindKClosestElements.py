def findClosestElements(arr, k, x):
    # right pointer is minus k bc we cant have a window that spills over
    l, r = 0, len(arr) - k

    while l < r:
        # m represents the left most value in the window
        m = (l + r) // 2
        # why the switch in subtracting x? Just how the math works out
        # Maybe becuase all the values on the left are less than x and the right are greater than
        # Line 11 fires if the num to the right of the window is closer to X
        if x - arr[m] > arr[m + k] - x:
            l = m + 1
        # Identified that the num at the beginning of the current window
          # is closer to X
        else:
              r = m
    return arr[l:l+k]

print(findClosestElements([1,2,3,4,5], 2, -1))
