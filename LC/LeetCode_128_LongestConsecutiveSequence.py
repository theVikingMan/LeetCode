def longestConsecutive(nums):
    maxLength = 0
    # Sets have constant look up time
    numSet = set(nums)

    # check every value in nums
    for num in nums:
        # check if we this is the beginning of a sequence by
        # having no left value
        if (num - 1  not in numSet):
            length = 0
            while (num + length in numSet):
                length += 1
            maxLength = max(maxLength, length)
    return maxLength