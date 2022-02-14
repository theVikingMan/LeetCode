
def solution(nums, k):
    n, k, j = len(nums), k % len(nums), 0
    while n > 0 and k % n != 0:
        for i in range(0, k):
            # swap
            nums[j + i], nums[len(nums) - k +
                              i] = nums[len(nums) - k + i], nums[j + i]
        n, j = n - k, j + k
        k = k % n
    return nums


print(solution([5, 6, 7, 1], 5))
# [5,6,7,1,2,3,4]
