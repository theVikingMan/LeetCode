def solution(boxes):
    ans = [0]*len(boxes)
    leftCount, leftCost, rightCount, rightCost, n = 0, 0, 0, 0, len(boxes)
    for i in range(1, n):
        if boxes[i-1] == '1':
            leftCount += 1
        leftCost += leftCount # each step move to right, the cost increases by # of 1s on the left
        ans[i] = leftCost
    for i in range(n-2, -1, -1):
        if boxes[i+1] == '1':
            rightCount += 1
        rightCost += rightCount
        ans[i] += rightCost
    return ans        

print(solution("001011"))


    # res = [0] * (len(boxes))
    # for i in range(len(boxes)):
    #     for y in range(len(boxes)):
    #         if y == i:
    #             continue
    #         elif y != i and (boxes[y] == "1"):
    #             if y < i:
    #                 res[i] = res[i] + (i-y)
    #             else:
    #                 res[i] = res[i] + (y-i)
    #         else:
    #             continue
    # return res
