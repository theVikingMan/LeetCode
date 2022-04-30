def characterReplacement(s, k):
    count = {}
    res = 0
    l = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        # The length of the interval keeps increasing no matter what char
        # The count keeps track of what is IN our substring
        # The max count should OFFSET the growing length unless we
          # encounter a non-max char but our interval keeps growing
        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res

print(characterReplacement('AABABBA', 1))