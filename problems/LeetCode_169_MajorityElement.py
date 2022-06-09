def majorityElement(nums):
    counter = 0
    result = 0

    for num in nums:
        if counter == 0: # if new number should be considered the most seen
            result = num
        if num != result: # instance which leads to the assumption that its not the most
            counter -= 1
        if num == result: # evidence the num is the majority
            counter += 1
    return result

print(majorityElement([1,1,2,3]))