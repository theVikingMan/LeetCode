import collections


def solution(s, t):
    dictA, dictB = [0] * 26, [0] * 26
    for letter in s:
        dictA[ord(letter) - ord('a')] += 1
    for letter in t:
        dictB[ord(letter) - ord('a')] += 1
    return dictA == dictB

print(solution('abb', 'abbb'))

# T: O(s * t)
# S: O(s * t)

# ------ OR ------ #

def solution(s, t):
  if len(s) != len(t):
    return False
  countS, countT = {}, {}
  for i in range(len(s)):
    countS[s[i]] = 1 + countS.get(s[i], 0)
    countT[t[i]] = 1 + countS.get(t[i], 0)

  return countS == countT

# T: O(s * t)
# S: O(s * t)

# ------ OR ------ #

def isAnagram(s, t):
  if len(s) != len(t):
    return False
  sCount, tCount = collections.Counter(s), collections.Counter(t)
  return sCount == tCount

# T: O(s * t)
# S: O(s * t)

# ------ OR ------ #

def solution(s, t):
  return (sorted(s) == sorted(t))

# T: O(s * log(s))
# S: O(1) -- if sorting is agreed not to have any space implications