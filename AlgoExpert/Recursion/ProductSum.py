def productSum(array, level=1):
    total = 0
    for elem in array:
        if isinstance(elem, list):
            total += (productSum(elem, level+1))
        else:
            total += elem
    return total * level


print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))