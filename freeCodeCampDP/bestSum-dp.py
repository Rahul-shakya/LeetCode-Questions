# bestSum
# from dynamic programming video YT
# https://www.youtube.com/watch?v=oBt53YbR9Kk&t=11470s
# https://leetcode.com/playground/Ux7hUcVM
# Timestamp: 01:52:06


def bestSumNoDP(target, arr):
    if target == 0:
        return []
    if target < 0:
        return None
    ans = None
    for num in arr:
        remainder = target - num
        result = bestSumNoDP(remainder, arr)
        if result is not None:
            result.append(num)
            if(ans == None or (len(result) < len(ans))):
                ans = result
    return ans


def bestSumDP(target, arr, memo = None):
    if(memo == None):
        memo = {}
    if(target in memo):
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    ans = None
    for num in arr:
        remainder = target - num
        result = bestSumDP(remainder, arr, memo)
        if(result is not None):
            combi = result + [num]
            if(ans == None or (len(combi) < len(ans))):
                ans = combi
    memo[target] = ans
    return ans



testCases = [(7, [2, 4, 3]), (7, [5, 3, 4, 7]), (7, [2, 4]), (8, [2, 3, 5]),(100,[1, 2, 5, 25])]

for test in testCases:
    targetSum, numbers = test
    print(f'bestSumDP({targetSum}, {numbers})={bestSumDP(targetSum, numbers)}')
