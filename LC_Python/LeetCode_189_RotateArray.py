
def solution(nums, k):
  n = len(nums)
  startIdx, count = 0, 0 # start will point to beginning of a cycle, count is num elems rotated

  while count < n: # Need to rotate one full length of the arr
    currIdx, prevElem = startIdx, nums[startIdx] # curr calcs next idx and if we need to alter rotataion in even length arr
    while True:
      nxt_idx = (currIdx + k) % n # calculate rotated place of current num
      nums[nxt_idx], prevElem = prevElem, nums[nxt_idx] # grab the next num and replace with the one we just picked up
      currIdx = nxt_idx # move forward
      count += 1 # mark that we have made one alteration
      if currIdx == startIdx: # if we have made it back without changing the whole array (even)
        break
    startIdx += 1 # if even length, start cycle on the next set
  return nums

print(solution([5, 6, 7, 1], 5))
