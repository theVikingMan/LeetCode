def runningSum(nums):
	res = []
	sum_nums = 0
	slow = 0
	for i in range(len(nums)):
		if i == 0:
			res.append(nums[i])
		else:
			sum_nums += nums[slow]
			res.append(nums[i] + sum_nums)
			slow += 1
	return res

print(runningSum([0]))

# LeetCode Discussion option 2 way to solve
def runningSum2(nums)
	result = []
	total = 0
	for i in range(len(nums)):
		total += nums[i]
		result.append(total)
	return result