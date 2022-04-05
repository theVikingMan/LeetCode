def spiralOrder(matrix):
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    res = []

    # Keep looping until one of the pointers crossed
    while top < bottom and left < right:
        # right to left
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        # top to bottom in the right column
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1

        if not (left < right and top < bottom):
            break

        # left to right in the bottom column
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1

        #bottom to top on the left column
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1
    return res


print(spiralOrder([[1,2,3,4]]))
