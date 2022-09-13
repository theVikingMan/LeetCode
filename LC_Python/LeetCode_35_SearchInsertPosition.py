def searchInsert(nums, target):
    if len(nums) == 0:
        return 0
    start = 0
    end = len(nums) - 1

    while start <= end:
        middle = (start + end) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            start = middle + 1
        elif nums[middle] > target:
            end = middle - 1
    return start

print(searchInsert([1,3,5,6], 0))
# print(searchInsert([1,3,5,6], 7))
# print(searchInsert([1,3,5,6], 5))
