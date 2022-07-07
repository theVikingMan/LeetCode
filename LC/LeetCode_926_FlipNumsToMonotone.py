def minFlipsMonoIncr(s: str):
    # ones array calculates count of "1"s on the left hand side of the index
    ones = [0] * (len(s))
    # zeros array calculates count of "0"s on the right hand side of the index
    zeros = [0] * (len(s))

    for i in range(1,len(s)):
        if s[i-1] == '1':
            ones[i] = 1 + ones[i-1]
        else:
            ones[i] = ones[i-1]
    for i in range(len(s)-2,-1,-1):
        if s[i+1] == '0':
            zeros[i] = 1 + zeros[i+1]
        else:
            zeros[i] = zeros[i+1]
    mini = len(s)
    for i in range(len(s)):
        mini = min(mini,zeros[i] + ones[i])
    return mini

# print(minFlipsMonoIncr('00110'))
print(minFlipsMonoIncr('011'))