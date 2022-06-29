def spiralTraverse(array):
    res = []

    l, r = 0, len(array[0])
    t, b = 0, len(array)
    while l < r and t < b:
        for i in range(l, r):
            res.append(array[t][i])
        t += 1

        for i in range(t, b):
            res.append(array[i][r - 1])
        r -= 1

        if not (l < r and t < b):
            break

        for i in range(r - 1, l - 1, -1):
            res.append(array[b - 1][i])
        b -= 1

        for i in range(b - 1, t - 1, -1):
            res.append(array[i][l])
        l += 1
    return res

# T: O(n) -> n is the number of elements in the array
# S: O(n) -> n is the number of elements in the array