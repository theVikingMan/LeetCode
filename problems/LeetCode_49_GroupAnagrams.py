import collections

def solution(strs):
  res = collections.defaultdict(list) # will append to list with same number of letters

  for s in strs:
    count = [0] * 26 # Holds num of letters for each word
    for c in s:
      count[ord(c) - ord('a')] += 1 # increases each letter count
    res[tuple(count)].append(s) # append word to corresponding key in dict
                                # lists cannot be keys so tuplize the count array
  return res.values() # .values() outputs an array

print(solution(["eat","tea","tan","ate","nat","bat"]))

# T: O(N * M) -> number of words times number of letters
# S: O(N) --> the output dictionary with the count array always constant at 26