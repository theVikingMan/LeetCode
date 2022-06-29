def isMonotonic(array):
    if len(array) < 2:
        return True
    inc, dec = True, True
    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            dec = False
        elif array[i] < array[i-1]:
            inc = False
    return (inc or dec)

print(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))

# T: O(n) -> n is the length of the array
# S: O(1)

# -------- SIMPLE -------- #
# def isMonotonic(array):
#   return(all(array[i] <= array[i+1] for i in range(len(array) - 1)) or
#          all(array[i] >= array[i+1] for i in range(len(array) - 1)))
