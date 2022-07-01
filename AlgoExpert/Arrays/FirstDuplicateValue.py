def firstDuplicateValue(array):
    seen = set()
    for n in array:
        if n in seen:
            return n
        seen.add(n)
    return -1

print(firstDuplicateValue([1, 2, 3, 1]))