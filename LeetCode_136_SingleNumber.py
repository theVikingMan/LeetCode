def singleNumber(nums):
	mapping = {}
	for num in nums:
			if num not in mapping:
					mapping[num] = 1
			else:
					mapping[num] += 1
	for key in mapping:
			if mapping[key] == 1:
					return key

print(singleNumber([2,2,1]))

# Bit manipulation
	# res = 0
	# for num in nums:
	# 		res = num ^ res
	# return res