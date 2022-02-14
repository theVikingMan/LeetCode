def subsets(nums):
    # Create a result array with the first element being an empty array
    result = [[]]
    # Loop through the given input
    for num in nums:
        # Loop again but we will want to loop over our result array
        # to add our current num (as an array) to all previous nums and their combinations
        for i in range(len(result)):
            result.append(result[i] + [num])
    #return our result variable
    return result

print(subsets([1, 2, 3]))