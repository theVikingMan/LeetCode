
def rotate(matrix):
    left, right = 0, len(matrix) - 1

    while left <= right:
        for i in range(right - left):
            top, bottom = left, right

            # store the top-left value
            topLeft = matrix[top][left + i]

            # bottom-left -> top-left
            matrix[top][left + i] = matrix[bottom - i][left]

            # bottom-right -> bottom-left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # top-right -> bottom-left
            matrix[bottom][right - i] = matrix[top + i][right]

            # top-left -> top-right
            matrix[top + i][right] = topLeft

        left += 1
        right -= 1
    return matrix

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))