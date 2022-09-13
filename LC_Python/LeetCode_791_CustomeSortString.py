def customeSortString(S, T):
    l = []

    for char in S:
        l.append(char*T.count(char))

    for char in T:
        if char not in l:
            l.append(char)

    return "".join(l)

print(customeSortString("kqep","pekeq"))