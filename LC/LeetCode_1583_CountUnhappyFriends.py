def solution(n, preferences, pairs):
    dd = {}
    ans = 0

    for one, two in pairs:
        dd[one] = preferences[one][:preferences[one].index(two)]
        dd[two] = preferences[two][:preferences[two].index(one)]

    for i in dd:
        for x in dd[i]:
            if i in dd[x]:
                ans += 1
                break

    return ans

print(solution(4, [ [1, 2, 3],
                    [3, 2, 0],
                    [3, 1, 0],
                    [1, 2, 0]],

                    [[0, 1],
                     [2, 3]]))