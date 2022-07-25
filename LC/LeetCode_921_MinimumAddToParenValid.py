class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = 0
        right = 0

        for p in s:
            if p == "(":
                left += 1
            elif p == ")" and left <= 0:
                right += 1
            else:
                left -= 1

        return left + right

def minAddToMakeValid(s):
  stack = []
  dict = {")":"("}

  for l in s:
    if not stack or l == "(" or stack[-1] != dict[l]:
      stack.append(l)
    else:
      stack.pop()
  return len(stack)