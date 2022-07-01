def arrayOfProducts(array):
    prefix = 1
    res = []
    for n in array:
        res.append(prefix)
        prefix *= n

    postfix = 1
    for i in range(len(array) - 1, -1, -1):
        res[i] *= postfix
        postfix *= array[i]
    return res

print(arrayOfProducts([5, 1, 4, 2]))