import collections

def solution(s):
  counts = collections.Counter(s)

  for i, l in enumerate(s):
    if counts[l] == 1:
      return i
  return -1