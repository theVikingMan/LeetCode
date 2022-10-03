
# ------------- Sliding Window ------------- #

def minSubArrLen(target, nums):
    output, leftPointer, currentSum = float('inf'), 0, 0

    for rightPointer in range(len(nums)):
      currentValue = nums[rightPointer]
      currentSum += currentValue
      while currentSum >= target:
        output = min(output, rightPointer - leftPointer + 1)
        leftValue = nums[leftPointer]
        currentSum -= leftValue
        leftPointer += 1

    return output if output != float("inf") else 0

# T: O(n) -> 2 pointer techniques are just considered 2 for-loops
# S: O(1) -> no auxiliary space, just constant 2 pointers