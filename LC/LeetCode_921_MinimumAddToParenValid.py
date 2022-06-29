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