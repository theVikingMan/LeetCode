def generateParenthesis(n):
    # create output variable
    result = []

    def backtracking(openPar, closedPar, curr):
        # base case: if we have the total number of paras to complete a set
        if (openPar == closedPar == n):
            result.append(curr)
            # dont return a result for this style of backtracking
            return

        if openPar < n:
            backtracking(openPar + 1, closedPar, curr + '(')

        if closedPar < openPar:
            backtracking(openPar, closedPar + 1, curr + ')')

    # begin with no open or closed paras and a temp (empty) string that
    # will be filled with paras but never held globally given how the solution is set up
    backtracking(0, 0, '')
    return result

'''
def generatePars(n):
    res = []
    stack = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return

        if openN < n:
            stack.append('(')
            backtrack(openN + 1, closedN)
            stack.pop()

        if closedN < openN:
            stack.append(')')
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0, 0)
    return res
'''

print(generateParenthesis(3))