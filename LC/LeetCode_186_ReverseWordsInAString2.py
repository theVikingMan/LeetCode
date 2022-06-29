class Solution:
  def reverseWords(self, s):
    l, r = 0, len(s) - 1

    while l < r: # reverse the sequence of words
      s[l], s[r] = s[r], s[l]
      l += 1
      r -= 1

    start = 0
    while start < len(s) - 1: # find the edge of each word and reverse them
      fast = start + 1
      while fast < len(s) and s[fast] != " ":
        fast += 1
      end = fast - 1
      while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
      start = fast + 1
    return s

test = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]

solution = Solution()
print(solution.reverseWords(test))