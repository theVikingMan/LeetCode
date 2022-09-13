def canPartition(nums):
    sumNums = sum(nums) # Reduce repeated work
    if sumNums % 2: # Answer must be even to be divided by 2
        return False

    dp = set()
    target = sumNums // 2
    dp.add(0) # initial value that allows for single number answer

    for n in nums: # Interate through all possible given values
        nextDP = set() # will keep all old products AND new products of the current given value
        for t in dp: # Interate through all of the products till now
            if (t + n) == target: # check if we found it, optimization
                return True
            nextDP.add(t + n) # add the new product to the to-be-new-all products set
            nextDP.add(t) # add the old product
        dp = nextDP
    return True if target in dp else False

print(canPartition([1,5,11,5]))

# T: O(n * m) --> n is the sumSubSets we make, m is the elements in nums
# S: O(n) --> constant space give only 1-2 sets at any given time


# --------- Recursive with Memoization --------- #

def canPartition(nums):
  total = sum(nums)
  if total % 2:
    return False
  target = total // 2
  memo = {}

  def helper(i, curr):
    if i == len(nums) or curr > target:
      return False
    if curr == target:
      return True
    if (i, curr) in memo:
      return memo[(i, curr)]

    memo[(i, curr)] = helper(i + 1, curr + nums[i]) or helper(i+1, curr)
    return memo[(i, curr)]
  return helper(0, 0)

print(canPartition([1,5,11,5]))
