import collections

def isPossible(nums):
  count = collections.Counter(nums)
  hypo = collections.defaultdict(int)

  for n in nums:
    if count[n] == 0:
      continue
    if hypo[n] > 0:
      hypo[n] -= 1
      hypo[n+1] += 1
      count[n] -= 1
    elif count[n] > 0 and count[n + 1] > 0 and count[n + 2] > 0:
      count[n] -= 1
      count[n+1] -= 1
      count[n+2] -= 1
      hypo[n+3] += 1
    else:
      return False
  return True

print(isPossible([1,2,3,3,4,4,5,5]))