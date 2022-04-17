def majorityElement(nums):
    counter = 0
    result = 0

    for num in nums:
        if counter == 0:
            result = num
        if num != result:
            counter -= 1
        if num == result:
            counter += 1
    return result

print(majorityElement([1,1,2,3]))