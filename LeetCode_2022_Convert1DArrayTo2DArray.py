def construct2DArray(original, r, c):
    result = []
    subset = []
    if r * c < len(original) or r * c > len(original):
        return result
    for idx, num in enumerate(original):
        subset.append(num)
        if ((idx + 1) % c) == 0:
            result.append(subset)
            subset = []
    return result


print(construct2DArray([1,2], 1, 1))