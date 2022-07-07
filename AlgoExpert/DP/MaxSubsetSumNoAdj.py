def maxSubsetSumNoAdjacent(array):
    one, two = 0, 0
    for num in array:
        temp = two
        two = max(two, one + num)
        one = temp
    return two

# T: O(n)
# S: O(1)

print(maxSubsetSumNoAdjacent([[75, 105, 120, 75, 90, 135]]))