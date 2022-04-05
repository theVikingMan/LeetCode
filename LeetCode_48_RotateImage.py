
def rotate(self, matrix):
    l, r = 0, len(matrix) - 1

    while l <= r:
        for i in range(r - l):
            top, bottom = l, r

            # handle top left
            topLeft = matrix[top][l + i]

            # handle bottom-left -> top-right
            matrix[top + i][l] = matrix[bottom][l + i]

            # handle bottom-right -> bottom-left
            matrix[bottom][l] = matrix[bottom][r]

            # handle top-right -> bottom-right
            matrix[bottom][r] = matrix[top][r]

            # handle top-left -> top right
            matrix[top][r] = topLeft

        l += 1
        r -= 1

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))