from shutil import move


def moveElementToEnd(array, toMove):
    l, r = 0, len(array) - 1
    while l < r:
        if array[l] == toMove:
            swap(l, r, array)
            r -= 1
        else:
            l += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))