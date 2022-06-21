def findPeakElement(nums):
    l, r = 0, len(nums) - 1

    while l < r:
        mid = (r + l) // 2
        if nums[mid] < nums[mid+1]: # still more larger nums
            l = mid + 1
        else: # potentially found the end of the increasing nums or at least in it
            r = mid
    return l

print(findPeakElement([1,2,1,3,5,6,4])) # Output: 5