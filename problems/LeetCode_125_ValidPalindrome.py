class Solution:
  def isPalindrome(s):
      res = ""
      for l in s:
          if l.isalpha():
              res += l.lower()
          if l.isnumeric():
              res += l
      left, right = 0, len(res) - 1
      while left < right:
          if res[left] != res[right]:
              return False
          left += 1
          right -= 1
      return True

test1 = "A man, a plan, a canal: Panama"
test2 = "0P"

print(Solution.isPalindrome(test1)) # true
print(Solution.isPalindrome(test2)) # false