
def solution(str1, str2):
    dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

    for j in range(len(str2) + 1):
        dp[len(str1)][j] = len(str2) - j
    for i in range(len(str1) + 1):
        dp[i][len(str2)] = len(str1) - i

    for i in range(len(str1) - 1, -1, -1):
        for j in range(len(str2) - 1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
    return dp[0][0]

print(solution("", "abc"))