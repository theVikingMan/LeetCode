import collections

def maxSlidingWindow(nums, k):
  q = collections.deque()
  res = []
  l = r = 0

  while r < len(nums):
    # Edit queue to have it in decreasing order
    while q and nums[q[-1]] < nums[r]:
      q.pop()
    q.append(r)

    # Remove the curr max if the window no longer includes its idx
    if q[0] < l:
      q.popleft()

    # edge case handling:
    if (r + 1) >= k:
      res.append(nums[q[0]])
      l += 1
    r += 1

  return res