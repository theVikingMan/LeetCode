def singleNumber(nums):
	single = []
	for num in nums:
		if num not in single:
			single.append(num)
		else:
			single.remove(num)
	return single.pop() # or my way of stack[0]

print(singleNumber([2,2,1]))


# LC was of using a hash table
"""from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table:
            if hash_table[i] == 1:
                return i"""

# interesting find with .get()
"""def singleNumber(nums):
	counts = dict()
	for i in nums:
	  counts[i] = counts.get(i, 0) + 1
	return counts"""