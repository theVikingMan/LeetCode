# -------------- Clean with Helper function -------------- #

class Solution:
  def search(self, nums, target):
      self.nums, self.target = nums, target
      return self.helper(0, len(nums)-1)

  def helper(self, low, high):
      if low > high: return -1
      mid = (high + low) // 2

      if self.target == self.nums[mid]: return mid
      elif self.target < self.nums[mid]: return self.helper(low, mid-1)
      else: return self.helper(mid+1, high)

# -------------- Classic implementation -------------- #

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = left + (right - left) // 2
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1


print(search([-1,0,3,5,9,12], 9))