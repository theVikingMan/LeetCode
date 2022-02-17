class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0

        while t_pointer < len(t):
            if s_pointer < len(s) and t[t_pointer] == s[s_pointer]:
                s_pointer += 1
            t_pointer += 1
        return s_pointer == len(s)