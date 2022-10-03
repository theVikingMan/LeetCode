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

def solution(strs):
  output = []
  groups = collections.defaultdict(list)

  for word in strs:
    groups[tuple(sorted(word))].append(word)

  for _, value in groups.items():
    output.append(value)

  return output

# T: O(N*K*log(K)) -> length of input array(N) * sorting for each word (length of each word is K)
# S: O(N) --> the output dictionary with the count array always constant at 26
