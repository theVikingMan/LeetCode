def letterCombinations(digits):
    result = []
    mapping = { '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'}

    def dfs(idx, subString):
        # Base case: if we have reached the length we need to add
        if (len(subString) == len(digits)):
            result.append(subString)
            return

        # go through all the digits at the index of the given string
        # this is basically a nested for-loop with the other loop being the recursion
        for c in mapping[digits[idx]]:
            # note, once a string is added, it will return nothing so it will
            # continue looping like it never added the next char
            dfs(idx + 1, subString + c)

    # handle edge case that we are given initially nothing
    if len(digits) < 1:
        return result

    dfs(0, "")
    return result

print(letterCombinations('23'))