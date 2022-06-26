import collections

class TimeMap:
  def __init__(self):
    self.store = collections.defaultdict(list) # key (str) : [[value, timestamp] of arrays]

  def set(self, key: str, value: str, timestamp: int) -> None:
    self.store[key].append([value, timestamp])

  def get(self, key: str, timestamp: int) -> str:
    res = ""
    arr = self.store.get(key, []) # get the set of values we need to look in
    l, r = 0, len(arr) - 1
    while l <= r:
      m = (l + r) // 2
      if arr[m][1] <= timestamp: # found a valid answer
        res = arr[m][0]
        l = m + 1 # can we find a more valid answer aka, higher timestamp
      else:
        r = m - 1 # values are too large, search smaller values for possible valid num
    return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)