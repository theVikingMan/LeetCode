def searchMatrix(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])
    top, bottom = 0, ROWS - 1

    # Search the for which row the num might! be in
    # Remember, that the rows and columns are all sorted, even start and end
    while top <= bottom:
        row = (top + bottom) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bottom = row - 1
        else:
            break

    if not (top <= bottom): # Need to check if our row checks didnt find it, pointers overlap
        return False

    l, r = 0, COLS - 1
    while l <= r: # run normal binary search on the indentified row
        m = (l + r) // 2
        if target == matrix[row][m]:
            return True
        elif target > matrix[row][m]:
            l = m + 1
        else:
            r = m - 1
    return False

print(searchMatrix([[-10,-10],[-9,-9],[-8,-6],[-4,-2],[0,1],[3,3],[5,5],[6,8]], 0))

