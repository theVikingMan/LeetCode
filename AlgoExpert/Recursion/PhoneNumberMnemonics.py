def phoneNumberMnemonics(phoneNumber):
    book = {
        '1': ['1'],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
        '0': ['0']
    }
    res = []

    def bt(i, curr):
        if len(curr) == len(phoneNumber):
            res.append(curr)
            return

        for l in book[phoneNumber[i]]:
            bt(i+1, curr + l)

    bt(0, '')
    return res

print(phoneNumberMnemonics('1905'))