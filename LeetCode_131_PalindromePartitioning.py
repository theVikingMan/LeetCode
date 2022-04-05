def partition(s):
    result = []
    part = []

    def dfs(i):
        # if we have gotten to the end of the string, add it
        if i >= len(s):
            # append copy as we will be mutating it later with other calls
            result.append(part[::])
            return

        # check all palindrome ranges almost like a sliding door
        for j in range(i, len(s)):
            # call our palindrome helper function on each segment starting at just one letter
            if isPalindrome(s, i, j):
                part.append(s[i:j+1])
                dfs(j+1)
                # undo decision to append
                part.pop()

    dfs(0)
    return result

def isPalindrome(s, l, r):
    # start on the ends and work in, checking the original string
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True

print(partition('aabaa'))