import collections
import heapq
# -------------- Max Heap -------------- #

def findKthLargest(nums, k):
  maxH = []
  res = 0
  for n in nums:
    maxH.append(-1 * n)
  heapq.heapify(maxH)

  while k:
    topE = heapq.heappop(maxH)
    res = -1 * topE
    k -= 1

  return res

# T: O(N * log(k)) -> Have to look at N elems and adding to heap is log(k)
# S: O(k) -> size of heap

print([3,2,1,5,6,4], 2)

# -------------- Quick Select -------------- #
# def findKthLargest(nums, k):
#   k = len(nums) - k

#   def quickselect(l, r):
#     pivot, p = nums[r], l
#     for i in range(l, r):
#       if nums[i] <= pivot:
#         nums[p], nums[i] = nums[i], nums[p]
#         p += 1
#     nums[p], nums[r] = nums[r], nums[p]

#     if p > k:
#       return quickselect(l, p - 1)
#     elif p < k:
#       return quickselect(p + 1, r)
#     else:
#       return nums[p]

#   return quickselect(0, len(nums) - 1)

