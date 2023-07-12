# howSum
# from dynamic programming video YT
# https://www.youtube.com/watch?v=oBt53YbR9Kk&t=11470s
# https://leetcode.com/playground/CvycqXzU
# Timestamp: 01:29:29

def func(target, numbers, memo = None):
    if memo is None:
        memo = {}
    if(target in memo):
        return memo[target]
    if(target == 0):
        return []
    if(target < 0):
        return None
    for currNum in numbers:
        remainingSum = target - currNum
        memo[target] = func(remainingSum, numbers, memo)
        if(memo[target] is not None):
            memo[target].append(currNum)
            return memo[target]
    return None
        
    
testCases = [(7, [2, 3]), (7, [5, 3, 4, 7]), (7, [2, 4]), (8, [3, 2, 5]), (300, [7, 14])]

for test in testCases:
    targetSum, numbers = test
    print(f'canSum({targetSum}, {numbers})={func(targetSum, numbers)}')


        
# print(func(7,[5,4,3,7]))
# print(func(7,[2,4]))
# print(func(8,[3,2,5]))
# print(func(300,[7,14]))
