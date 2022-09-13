def backspaceCompare(s, t):
    def build(string):
        ans = []
        for c in string:
            if c != '#':
                ans.append(c)
            else:
                ans.pop() if ans else '#'
        "".join(ans)
        return ans

    return build(s) == build(t)