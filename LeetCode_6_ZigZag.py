'''
Solution #1

def covert(s, numRows):
    row = 0
    res = [[] for i in range(numRows)]
    delta = -1

    if numRows == 1 or numRows >= len(s):
        return s

    for c in s:
        res[row].append(c)
        if row == 0 or row ==numRows - 1:
            delta *= -1
        row += delta

    for i in range(len(res)):
        res[i] = "".join(res[i])
    return ''.join(res)
'''

# Solution #2
def covert(s, numRows):
    if numRows == 1:
        return s

    cycle = (2 * numRows) - 2
    res = []
    for i in range(numRows):
        for j in range(i, len(s), cycle):
            res.append(s[j])
            k = j + cycle - 2 * i
            if i != 0 and i != numRows - 1 and k < len(s):
                res.append(s[k])
    return "".join(res)


print(covert("PAYPALISHIRING", 3))

'''
P   A     H   N  ["PAHN"]
A P L  S  I I G  ["APLSIIG]
Y   I     R      ["YIR]

Cycle = 3 * 2 - 2 = 4

'''