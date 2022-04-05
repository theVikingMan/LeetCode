def majorityElement(nums):
    res, count = 0, 0
    for n in nums:
        if count == 0:
            res = n
        count += (1 if n == res else -1)
    return res

print(majorityElement([1,1,2,3]))

# def majorityElement(nums):
#     mapping = {}
#     maxFreq, maxNum = 0, 0
#     for n in nums:
#         mapping[n] = 1 + mapping.get(n, 0)
#         maxNum = n if mapping[n] > maxFreq else maxNum
#         maxFreq = max(mapping[n], maxFreq)
#     return maxNum