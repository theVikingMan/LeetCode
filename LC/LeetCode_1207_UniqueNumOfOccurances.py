import collections

def uniqueOccurrences(arr):
  count = collections.Counter(arr)
  seen = set()
  for key, value in count.items():
    if value not in seen:
      seen.add(value)
    else:
      return False
  return True

# ----- Alt way (little slower just in compiling) -------- #

def uniqueOccurrences(arr):
  return len(set(arr)) == len(set(collections.Counter(arr).values()))