def letterCasePermutation(S):
    ans = [[]]

    for char in S:
        n = len(ans)
        if char.isalpha():
            for i in range(n):
                ans.append(ans[i][:])
                ans[i].append(char.lower())
                ans[n+i].append(char.upper())
        else:
            for i in range(n):
                ans[i].append(char)

    return ["".join(x) for x in ans]

print(letterCasePermutation('a1b2'))


# RECURSIVE SOLUTION
# ------------------
# def letterCasePermutation(self, s: str) -> List[str]:
#     return self.helper(s, "", [])

# def helper(self, s: str, current: str, solution:List[str]) -> List[str]:
#     if len(s)==0:
#         solution.append(current)
#         return solution
#     if s[0].isalpha():
#         self.helper(s[1:], current+s[0].lower(), solution)
#         self.helper(s[1:], current+s[0].upper(), solution)
#     else:
#         self.helper(s[1:], current+s[0], solution)
#     return solution