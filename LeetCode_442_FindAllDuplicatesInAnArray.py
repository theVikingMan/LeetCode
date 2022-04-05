def findDuplicates(nums):
    result = []
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] < 0:
            result.append(index + 1)
        nums[index] = -nums[index]
    return result

print(findDuplicates([4,3,2,7,8,2,3,1]))
print(findDuplicates([1, 2, 1]))
print(findDuplicates([1]))