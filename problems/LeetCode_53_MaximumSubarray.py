def max_array(nums):
    max_subarray = current_subarray = nums[0]
    for num in nums[1:]:
        current_subarray = max(num, current_subarray + num)
        max_subarray = max(max_subarray, current_subarray)
    return max_subarray

print(max_array([-2,1,-3,4,-1,2,1,-5,4]))
