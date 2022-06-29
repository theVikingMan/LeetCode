
def solution(nums, k):
  n = len(nums)

  start, count = 0, 0 # start will point to beginning of a cycle, count is num times rotated
  while count < n: # Need to rotate one full length of the arr
    curr, prev = start, nums[start] # curr calcs next idx and if we need to alter rotataion in even length arr
    while True:
      nxt_idx = (curr + k) % n # calculate rotated place of current num
      nums[nxt_idx], prev = prev, nums[nxt_idx] # grab the next num and replace with the one we just picked up
      curr = nxt_idx # move forward
      count += 1 # mark that we have made one alteration
      if curr == start: # if we have made it back without changing the whole array (even)
        break
    start += 1 # start cycle on the next set
  return nums

print(solution([5, 6, 7, 1], 5))
