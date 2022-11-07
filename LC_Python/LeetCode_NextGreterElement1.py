
def nextGreaterElement(nums1, nums2):
  nums1Idx = {n:i for i, n in enumerate(nums1)}
  res = [-1] * len(nums1)

  stack = []
  for i in range(len(nums2)):
    curr = nums2[i]
    while stack and curr > stack[-1]:
      val = stack.pop()
      res[nums1Idx[val]] = curr
    if curr in nums1Idx:
      stack.append(curr)
  return res

# Time: O(n + m) -> loop over nums2 (M) once and over nums1 (N) once
# Space: O(n) -> only stack the values in nums1

'''
def nextGreaterElement(nums1, nums2):
  greaterThan = {}
  for i in range(len(nums2) - 1, -1, -1):
    num = nums2[i]
    if i == len(nums2) - 1:
      greaterThan[num] = -1
      continue
    rightNum = nums2[i+1]
    if rightNum > num:
      greaterThan[num] = rightNum
      continue
    nextNum = greaterThan[rightNum]
    while nextNum != -1 and nextNum <= num:
      nextNum = greaterThan[nextNum]

    greaterThan[num] = nextNum

  output = []
  for n in nums1:
    output.append(greaterThan[n])

  return output
'''