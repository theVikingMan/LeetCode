def searchRange(nums, target):
  def findBounds(arr, isLower):
    n = len(arr)
    l, r = 0, n - 1
    while l <= r:
      mid = l + ((r - l) // 2)
      if arr[mid] == target: # found a valid element
        if isLower: # looking for lower bound
          if mid - 1 == -1 or arr[mid-1] != target: # start of arr or no valid elems to the left
            return mid
          r = mid - 1 # move search further left to find smallest starting point
        else: # looking for upper bound
          if mid + 1 == n or arr[mid+1] != target:
            return mid
          l = mid + 1
      elif arr[mid] < target:
        l = mid + 1
      else:
        r  = mid - 1
    return -1 # no valid elements were found, return desired null value

  first = findBounds(nums, True)
  if first == -1:
    return [-1,-1]
  second = findBounds(nums, False)
  return [first, second]


print(searchRange([5,7,7,8,8,10], 8))