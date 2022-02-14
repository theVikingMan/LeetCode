'''
def numIdenticalPairs(nums):
    ans = 0
    if not nums:
        return 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if (nums[i] == nums[j]) and (i < j):
                ans += 1
            continue
    return ans
'''

def numIdenticalPairs(nums):
    hashMap = {}
    res = 0
    for number in nums:            
        if number in hashMap:
            res += hashMap[number]
            hashMap[number] += 1
        else:
            hashMap[number] = 1
    return res

print(numIdenticalPairs([1,2,3,1,1,3]))