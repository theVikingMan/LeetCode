import collections

def isPossible(nums):
  count = collections.Counter(nums)
  hypo = collections.defaultdict(int)

  for n in nums:
    if count[n] == 0: # used up all the instances of the num
      continue
    if hypo[n] > 0: # have a prev sequenece to add on to the end
      hypo[n] -= 1
      hypo[n+1] += 1
      count[n] -= 1
    elif count[n] > 0 and count[n + 1] > 0 and count[n + 2] > 0: # found a sequence
      count[n] -= 1
      count[n+1] -= 1
      count[n+2] -= 1
      hypo[n+3] += 1
    else:
      return False
  return True

print(isPossible([1,2,3,3,4,4,5,5]))