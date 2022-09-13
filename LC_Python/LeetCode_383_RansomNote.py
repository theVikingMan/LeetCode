import collections

def solution(ransomNote, magazine):
  if len(ransomNote) > len(magazine):
    return False
  countmagazine = {}
  for l in magazine:
    countmagazine[l] = 1 + countmagazine.get(l, 0)

  for l in ransomNote:
    if l not in countmagazine or countmagazine[l] == 0:
      return False
    countmagazine[l] -= 1
  return True

print(solution('agg', 'efjbdg'))


# ---------- Another Way w/ Counter --------- #

# def solution(ransomNote, magazine):
#   countA, countB = collections.Counter(ransomNote), collections.Counter(magazine)
#   for key, value in countA.items():
#     if countA[key] > countB[key]:
#       return False
#   return True