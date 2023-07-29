# bestSum
# from dynamic programming video YT
# https://www.youtube.com/watch?v=oBt53YbR9Kk&t=11470s
# https://leetcode.com/playground/Ux7hUcVM
# Timestamp: 01:52:06


def bestSumNoDP(target, arr, ans = None):
    if ans is None:
        ans = 0
    if target == 0:
        return 1
    if target < 0:
        return None
    for num in arr:
        remainder = target - num
        result = bestSumNoDP(remainder, arr, ans)
        if result is not None:
            combi = result 
            if(ans < combi):
                ans += combi
    return ans


testCases = [(7, [4, 3, 2])]

for test in testCases:
    targetSum, numbers = test
    print(f'bestSumNoDP({targetSum}, {numbers})={bestSumNoDP(targetSum, numbers)}')
